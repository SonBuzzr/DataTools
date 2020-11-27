# Check the url status
import requests

import CSV_Read_Write

ErList = []
# check metadata link list
csvFile = "DownloadListRDS.csv"

# generate error list of N/A metadata
outputFile = "Metadata_ERRORLIST.csv"


def checkLink(args):
    URL = 'http://rds.icimod.org/Home/DataDetail?metadataId=' + str(args)
    response = requests.get(URL)
    # print(response.status_code)

    if not response.status_code == 200:
        print("Not Found.", URL)
        ErList.append(URL)
    # else:
    #     print(" Working")


csvData = CSV_Read_Write.readCSV_pd(csvFile)

for index, row in csvData.iterrows():
    m_id = row['MetadataID']
    m_uuid = row['MetadataUUID']

    checkLink(m_id)

heading = {'ErrorLink': ErList}
CSV_Read_Write.writeCSV_pd(outputFile, **heading)
