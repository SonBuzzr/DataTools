#  update the metadata info

import sys
from xml.dom import minidom
import GN_Login
import CSV_Read_Write

csvFile = 'SearchList.csv'

outputFile = 'Metadata Info.csv'

search_value = 'Mr. Basanta Shrestha'
replace_value = ' '

# for multilevel xml
mainNode = "gmd:pointOfContact"
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


# Get the value of multilevel node
def multiNodeInfo(*args):
    topNode = args[4].getElementsByTagName(args[0])

    for first in topNode:
        firstNodeTag = first.getElementsByTagName(args[1])

        for second in firstNodeTag:
            secondNodeTag = second.getElementsByTagName(args[2])

            for name in secondNodeTag:
                cName = name.getElementsByTagName(args[3])[0]

                if cName.childNodes.length > 0 and cName.childNodes[0].nodeValue == search_value:
                    print('Updating {}'.format(cName.childNodes[0].nodeValue))
                    cName.childNodes[0].nodeValue = replace_value
                    return args[4]

                else:
                    print("Match not found")
                    return args[4]


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

        metadata_author = multiNodeInfo(mainNode, firstNode, individualNametag, mText, metadataXML)
        # print(metadata_author.toxml())

        update_gn_xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                        <request><id>" + str(args[0]) + "</id><version>1</version>\
                       <data><![CDATA[" + metadata_author.toxml() + "]]></data></request>"
        # print(update_gn_xml)

        GN_CONN = GN_Login.gn_session.post(GN_Login.gn_update, data=update_gn_xml, headers=GN_Login.xml_header)

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
