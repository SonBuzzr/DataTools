#  update the metadata info

import sys
from xml.dom import minidom

import GN_Login
import CSV_Read_Write

csvFile = 'SearchList.csv'

outputFile = 'Metadata Info.csv'

author = 'Mr. Govinda Joshi'
position = 'Senior Cartographer/GIS Analyst'

voice = '977-1-5275222'
fax = "977-1-5275238"

replace_value = ' '

# for multilevel xml
# gmd:contact, gmd:pointOfContact, gmd:citedResponsibleParty
mainNode = "gmd:contact"
firstNode = "gmd:CI_ResponsibleParty"

# xml tag name
# add more tag to get more info
titleTag = "gmd:title"
abstractTag = "gmd:abstract"
purposeTag = "gmd:purpose"
individualNametag = "gmd:individualName"
positionName = "gmd:positionName"

# get value
mText = "gco:CharacterString"
mDate = "gco:DateTime"


def update_node_value(*args):
    topNode = args[4].getElementsByTagName(args[0])

    for first in topNode:
        firstNodeTag = first.getElementsByTagName(args[1])

        for second in firstNodeTag:
            secondNodeTag = second.getElementsByTagName(args[2])

            for name in secondNodeTag:
                cName = name.getElementsByTagName(args[3])[0]

                if cName.childNodes.length > 0 and cName.childNodes[0].nodeValue == args[5]:
                    print('Updating {}'.format(cName.childNodes[0].nodeValue))
                    cName.childNodes[0].nodeValue = replace_value
                    return args[4]

                else:
                    # print("Match not found")
                    return args[4]


# Get the value of multilevel node
def multiNodeInfo(*args):
    topNode = args[4].getElementsByTagName(args[0])
    if topNode.length > 0:
        print("Node")
        try:

            for first in topNode:
                firstNodeTag = first.getElementsByTagName(args[1])

                for second in firstNodeTag:
                    secondNodeTag = second.getElementsByTagName(args[2])

                    for name in secondNodeTag:
                        cName = name.getElementsByTagName(args[3])[0]

                        if cName.childNodes.length > 0 and cName.childNodes[0].nodeValue == args[5]:
                            print('Updating {}'.format(cName.childNodes[0].nodeValue))
                            cName.childNodes[0].nodeValue = replace_value
                            return args[4]

                        else:
                            # print("Match not found")
                            return args[4]
        except IOError:
            print(sys.exc_info()[0], "Error in accessing metadata with ID :" + str(m_id))


# Get the value of single node
def getNodeInfo(*args):
    topNode = args[2].getElementsByTagName(args[0])

    for first in topNode:
        firstNodeTag = first.getElementsByTagName(args[1])[0]

        if firstNodeTag.childNodes.length > 0:
            meta_value = firstNodeTag.childNodes[0].nodeValue
            return meta_value


def getInfo(*args):
    try:
        getXml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                    <request><uuid>" + args[1] + "</uuid></request>"

        GN_CONN = GN_Login.gn_session.post(GN_Login.gn_getURL, data=getXml, headers=GN_Login.xml_header)

        metadataXML = minidom.parseString(GN_CONN.text)
        # print(metadataXML)
        try:
            metadata_thumb = getNodeInfo("gmd:graphicOverview",)
            # metadata_author = update_node_value(mainNode, firstNode, individualNametag, mText, metadataXML, author)
            # metadata_position = update_node_value(mainNode, firstNode, positionName, mText, metadata_author, position)
            # update_gn_xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
            #                         <request><id>" + str(args[0]) + "</id><version>1</version>\
            #                        <data><![CDATA[" + metadata_author.toxml() + "]]></data></request>"

            # GN_CONN = GN_Login.gn_session.post(GN_Login.gn_update, data=update_gn_xml, headers=GN_Login.xml_header)
            print("Metadata Updated...", GN_CONN)
        except:
            print("Main tag not found ...")
        # metadata_author = multiNodeInfo_update(mainNode, firstNode, individualNametag, mText, metadataXML, author)
        # metadata_position = multiNodeInfo_update(mainNode, firstNode, positionName, mText, metadata_author, position)
        # print(metadata_position.toxml())

        # print(update_gn_xml)

    except IOError:
        print(sys.exc_info()[0], "Error in accessing metadata with ID :" + str(m_id))


csvData = CSV_Read_Write.readCSV_pd(csvFile)
GN_Login.gn_login()

for index, row in csvData.iterrows():
    m_id = row['Metadata ID']
    m_uuid = row['UUID']
    print(row['Metadata ID'], row['UUID'])
    getInfo(m_id, m_uuid)
GN_Login.gn_logout()
print("Update Completes ...")
