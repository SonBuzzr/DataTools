# Search geonetwork using free text, keywords, category
# creates a csv list of search metadata with ID and UUID

import xml.dom.minidom
from xml.dom.minidom import parse, parseString
import GN_Login
import CSV_Read_Write

# searching parameters in Geonetwork
search_text = ""
search_category = "datasets"
group = ""

search_result_ID = []
search_result_UUID = []

outputFile = 'SearchList.csv'


# get the value of node and append it in search result
def get_meta(gn_value, app_value):
    for values in gn_value:
        result = values.firstChild.data
        app_value.append(result)


def gn_search_metadata():
    xml_search = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><request><any>" + search_text + \
                 "</any><category>" + search_category + "</category><group>" + group + "</group></request>"
    GN_Login.gn_login()

    search_result = 0
    print("Searching Metadata...")
    gn_conn = GN_Login.gn_session.post(GN_Login.gn_search, data=xml_search, headers=GN_Login.xml_header)
    meta_xml = xml.dom.minidom.parseString(gn_conn.text)

    gn_uuid = meta_xml.getElementsByTagName("uuid")
    gn_id = meta_xml.getElementsByTagName("id")

    get_meta(gn_uuid, search_result_UUID)
    get_meta(gn_id, search_result_ID)

    GN_Login.gn_logout()

    for x, y in zip(search_result_ID, search_result_UUID):
        try:
            search_result = search_result + 1
        except ValueError as e:
            print(e)
    print("Metadata Search Result: ", search_result)


gn_search_metadata()

Search = {'Metadata ID': search_result_ID, 'UUID': search_result_UUID}
# print(search_result_ID, search_result_UUID)
CSV_Read_Write.writeCSV_pd(outputFile, **Search)
