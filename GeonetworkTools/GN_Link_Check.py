import CSV_Read_Write
import requests

csvFile = 'GetInfoList.csv'

csvData = CSV_Read_Write.readCSV_pd(csvFile)
error_list = []


def check_link(args):
    link_url = 'http://rds.icimod.org/Home/DataDetail?metadataId=' + str(args)
    response = requests.get(link_url)
    print(response.request.url)
    if not response.status_code == 200:
        error_list.append(link_url)


for index, row in csvData.iterrows():
    m_id = row['MetadataID']
    m_uuid = row['MetadataUUID']
    # print(row['Metadata ID'])
    check_link(m_id)

print(error_list)
