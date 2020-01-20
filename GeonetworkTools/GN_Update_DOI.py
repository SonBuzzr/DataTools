from xml.dom import minidom
import GN_Login
import CSV_Read_Write
from bs4 import BeautifulSoup
import requests
import sys


csvFile = 'SearchList.csv'

mainNode = "gmd:MD_LegalConstraints"
firstNode = "gmd:useLimitation"

# get value
mText = "gco:CharacterString"
mDate = "gco:DateTime"


def formatCitation(link):
    # print(link)
    headers = {
        'Accept': 'text/x-bibliography; style=apa-6th-edition',
    }

    response = requests.get(link, headers=headers)
    # print(response.text)
    remove_tag = BeautifulSoup(response.text, 'lxml').text
    # print(remove_tag)

    return remove_tag


def appendNode(*args):
    print("Updating node...")

    nodeString = """<?xml version="1.0" encoding="UTF-8"?>
                     <gmd:MD_Metadata xmlns:gmd="http://www.isotc211.org/2005/gmd"
                                      xmlns:gco="http://www.isotc211.org/2005/gco"
                                      xmlns:gts="http://www.isotc211.org/2005/gts"
                                      xmlns:gml="http://www.opengis.net/gml"
                                      xmlns:geonet="http://www.fao.org/geonetwork"
                                      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                                      xsi:schemaLocation="http://www.isotc211.org/2005/gmd
                                      http://www.isotc211.org/2005/gmd/gmd.xsd http://www.isotc211.org/2005/srv
                                      http://schemas.opengis.net/iso/19139/20060504/srv/srv.xsd">
                             <gmd:useLimitation>
                                <gco:CharacterString>Free to use with attribution to the source. Suggested citation: """ \
                 + args[1] + """</gco:CharacterString>
                            </gmd:useLimitation>
                    </gmd:MD_Metadata>
                """

    addXml = minidom.parseString(nodeString)
    intNode = args[0].getElementsByTagName(mainNode)[0]
    nodeUpdate = addXml.getElementsByTagName(firstNode)[0]

    refNode = intNode.getElementsByTagName(firstNode)[0]
    intNode.insertBefore(nodeUpdate, refNode)

    return args[0]


def updateNode(*args):
    # print(args[0], args[1])
    citationLink = formatCitation(args[1])
    # print(citationLink)
    topNode = args[0].getElementsByTagName(mainNode)

    for first in topNode:
        firstNodeTag = first.getElementsByTagName(firstNode)

        for second in firstNodeTag:
            secondNodeTag = second.getElementsByTagName(mText)[0]
            # print(len(secondNodeTag.childNodes[0]))

            # Update user limitation if it's empty
            if not secondNodeTag.childNodes.length:
                print("Empty use limitation ")
                update_limitation = appendNode(args[0], citationLink)

            else:
                print("Found use limitation")
                # print(secondNodeTag.childNodes[0].nodeValue)

    return args[0]


def getInfo(*args):
    try:
        getXml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                    <request><uuid>" + args[1] + "</uuid></request>"

        GN_CONN = GN_Login.gn_session.post(GN_Login.gn_getURL, data=getXml, headers=GN_Login.xml_header)
        metadataXML = minidom.parseString(GN_CONN.text)

        updateXML = updateNode(metadataXML, args[2])

        # print(updateXML.toxml())
        # print(args[0], args[1])
        
        update_gn_xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                <request><id>" + str(args[0]) + "</id><version>1</version>\
               <data><![CDATA[" + updateXML.toxml() + "]]></data></request>"
        # print(update_gn_xml)

        GN_CONN = GN_Login.gn_session.post(GN_Login.gn_update, data=update_gn_xml, headers=GN_Login.xml_header)

    except IOError:
        print(sys.exc_info()[0], "Error in accessing metadata with ID :" + str(m_id))


csvData = CSV_Read_Write.readCSV_pd(csvFile)
GN_Login.gn_login()
for index, row in csvData.iterrows():
    m_id = row['Metadata ID']
    m_uuid = row['UUID']
    m_doi = row['DOI']
    # print(row['Metadata ID'], row['UUID'])
    getInfo(m_id, m_uuid, m_doi)
GN_Login.gn_logout()
