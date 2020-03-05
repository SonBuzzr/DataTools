# update the user limitation with doi

from xml.dom import minidom
import GN_Login
import CSV_Read_Write
from bs4 import BeautifulSoup
import requests
import sys

csvFile = 'GN_DOI_NodeUpdateList.csv'

legalNode = "gmd:MD_LegalConstraints"
ulNode = "gmd:useLimitation"
charNode = "gco:CharacterString"


# Get citation text in APA style
def formatCitation(link):
    # print(link)
    headers = {
        'Accept': 'text/x-bibliography; style=apa',
    }

    response = requests.get(link, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    soup.i.unwrap()

    return soup.text


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
                                <gco:CharacterString>Free not to use with attribution to the source. Suggested citation: """ \
                 + args[1] + """</gco:CharacterString>
                            </gmd:useLimitation>
                    </gmd:MD_Metadata>
                """

    addXml = minidom.parseString(nodeString)
    intNode = args[0].getElementsByTagName(legalNode)[0]
    nodeUpdate = addXml.getElementsByTagName(ulNode)[0]

    intNode.insertBefore(nodeUpdate, intNode.firstChild)

    return args[0]


def updateNode(*args):
    # print(args[0], args[1])
    citationLink = formatCitation(args[1])
    # print(citationLink)
    topNode = args[0].getElementsByTagName(legalNode)

    # Loop through each and every child node
    for firstChild in topNode:
        fChild = firstChild.getElementsByTagName(ulNode)

        # Check if node has child or not
        if not fChild.length:
            print("No child node adding New Node ...")
            addUL = appendNode(args[0], citationLink)

        #  List all the child node value
        else:
            for i, child in enumerate(fChild):
                # print("index {}, value {}".format(i, child))
                lastChild = child.getElementsByTagName(charNode)[0]

                # check for blank user limitation
                # Remove child of the node with empty field
                # Create updated user limitation node
                if not lastChild.childNodes.length:
                    print("Removing empty node with index {} and appending value ...".format(i))
                    fChild[i].parentNode.removeChild(fChild[i])
                    appendUL = appendNode(args[0], citationLink)
                else:
                    print("Node values: {} with index {}".format(lastChild.childNodes[0].nodeValue, i))

    return args[0]


def getInfo(*args):
    try:
        getXml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                    <request><uuid>" + args[1] + "</uuid></request>"

        GN_CONN = GN_Login.gn_session.post(GN_Login.gn_getURL, data=getXml, headers=GN_Login.xml_header)

        # Parsing xml
        metadataXML = minidom.parseString(GN_CONN.text)

        updateXML = updateNode(metadataXML, args[2])

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

    getInfo(m_id, m_uuid, m_doi)

GN_Login.gn_logout()
