import urllib3
import csv, os, requests, sys


# http://rds.icimod.org:8080/geonetwork/srv/api/records/b9d32c94-ae11-4bcc-a26d-ce58c4db224c/formatters/xsl-view?output=pdf&language=eng&approved=true
# http://rds.icimod.org:8080/geonetwork/srv/api/records/4466ff60-ca1d-4c8d-ad6a-57145c35dda3/formatters/xml
def get_pdf_xml(ID, UUID):
    metadata_id = ID
    # url_pdf = 'http://rds.icimod.org:8080/geonetwork/srv/eng/pdf?id=' + str(metadata_id)
    url_pdf = 'http://rds.icimod.org:8080/geonetwork/srv/api/records/' + str(
        UUID) + '/formatters/xsl-view?output=pdf&language=eng&approved=true'
    # url_xml = 'http://rds.icimod.org:8080/geonetwork/srv/eng/xml_iso19139?id=' + str(metadata_id)
    url_xml = 'http://rds.icimod.org:8080/geonetwork/srv/api/records/' + str(UUID) + '/formatters/xml'

    http = urllib3.PoolManager()
    filename_pdf = 'xml_pdf_files/metadata_' + str(metadata_id) + '.pdf'
    filename_xml = 'xml_pdf_files/metadata_' + str(metadata_id) + '.xml'

    response = http.request('GET', url_pdf)
    with open(filename_pdf, 'wb')as f:
        f.write(response.data)

    response = http.request('GET', url_xml)
    with open(filename_xml, 'wb')as f:
        f.write(response.data)

    response.release_conn()


with open('metadata_id_uuid.csv', 'r') as f:
    spamreader = csv.reader(f, delimiter=' ', quotechar='|')
    for row in spamreader:
        output = (', '.join(row))
        ID = output.split(',')[0]
        UUID = output.split(",")[1]
        # print (ID + " : " + UUID)
        get_pdf_xml(ID, UUID)
