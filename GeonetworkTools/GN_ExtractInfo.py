# using minidom to extract information from online geonetwork system

import sys
from xml.dom import minidom
import GN_Login
import CSV_Read_Write

csvFile = 'SearchList.csv'
rdsLink = 'http://rds.icimod.org/Home/DataDetail?metadataId='

outputFile = 'Metadata Info.csv'

# for multilevel xml
mainNode = "gmd:contact"
firstNode = "gmd:CI_ResponsibleParty"

# xml tag name
# add more tag to get more info
titleTag = "gmd:title"
abstractTag = "gmd:abstract"
purposeTag = "gmd:purpose"
individualNametag = "gmd:individualName"
dateStampTag = "gmd:dateStamp"

# get value
mText = "gco:CharacterString"
mDate = "gco:DateTime"

title_info = []
abstract_info = []
purpose_info = []
author_info = []
date_info = []
id_info = []
uuid_info = []
link_info = []


# Get the value of multilevel node
def multiNodeInfo(*args):
    topNode = args[4].getElementsByTagName(args[0])

    for first in topNode:
        firstNodeTag = first.getElementsByTagName(args[1])

        for second in firstNodeTag:
            secondNodeTag = second.getElementsByTagName(args[2])

            for name in secondNodeTag:
                cName = name.getElementsByTagName(args[3])[0]

                if cName.childNodes.length > 0:
                    meta_value = cName.childNodes[0].nodeValue
                    return meta_value


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
                    <request><uuid>" + m_uuid + "</uuid></request>"

        GN_CONN = GN_Login.gn_session.post(GN_Login.gn_getURL, data=getXml, headers=GN_Login.xml_header)

        metadataXML = minidom.parseString(GN_CONN.text)
        # print(metadataXML)

        metadata_id = m_id
        metadata_uuid = m_uuid
        metadata_title = getNodeInfo(titleTag, mText, metadataXML)
        metadata_year = getNodeInfo(dateStampTag, mDate, metadataXML)
        metadata_author = multiNodeInfo(mainNode, firstNode, individualNametag, mText, metadataXML)
        metadata_abstract = getNodeInfo(abstractTag, mText, metadataXML)
        metadata_purpose = getNodeInfo(purposeTag, mText, metadataXML)
        metadata_link = rdsLink + str(m_id)

        id_info.append(metadata_id)
        uuid_info.append(metadata_uuid)
        title_info.append(metadata_title)
        date_info.append(metadata_year)
        author_info.append(metadata_author)
        abstract_info.append(metadata_abstract)
        purpose_info.append(metadata_purpose)
        link_info.append(metadata_link)

    except IOError:
        print(sys.exc_info()[0], "Error in accessing metadata with ID :" + str(m_id))


csvData = CSV_Read_Write.readCSV_pd(csvFile)
GN_Login.gn_login()
for index, row in csvData.iterrows():
    m_id = row['Metadata ID']
    m_uuid = row['UUID']
    # print(row['Metadata ID'], row['UUID'])
    getInfo(m_id, m_uuid)
GN_Login.gn_logout()

Information = {'ID': id_info, 'UUID': uuid_info, 'Title': title_info, 'Date': date_info,
               'Author': author_info, 'Abstract': abstract_info, 'Purpose': purpose_info, 'Link': link_info}

CSV_Read_Write.writeCSV_pd(outputFile, **Information)
