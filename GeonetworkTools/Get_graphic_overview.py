import csv, os, requests, sys
from xml.dom.minidom import parse, parseString
import xml.dom.minidom
from xml.dom import minidom

# RDS Credentials
gn_URL = "http://rds.icimod.org:8080"
gn_loginURL = "/geonetwork/j_spring_security_check"
gn_logoutURL = "/geonetwork/j_spring_security_logout"
gn_getURL = "/geonetwork/srv/eng/xml.metadata.get"

header_xml1 = {'Content-Type': 'application/xml'}

meta_id = []
meta_uuid = []
meta_thumbname = []

# Admin Credentials
payload = {'username': 'Samir', 'password': 'Ge0ne!RDS'}

# GN Login URL
log_in = gn_URL + gn_loginURL

# GN Logout URL
log_out = gn_URL + gn_logoutURL

# GN Namespace link
namespace = 'http://www.isotc211.org/2005/gmd/'

count = 0


def get_thumb(ID, UUID):
    try:
        get_metadata_URL = gn_URL + gn_getURL
        get_xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                <request><uuid>" + UUID + "</uuid></request>"
        conn = requests.Session()

        # GN Login
        conn_link = conn.post(log_in, data=payload)
        conn_link = conn.post(get_metadata_URL, data=get_xml, headers=header_xml1)

        meta_xml = minidom.parseString(conn_link.text)

        meta_thumbnail_node = meta_xml.getElementsByTagName("gmd:graphicOverview")
        m_thumb = ""
        m_thumb_url = ""

        for node in meta_thumbnail_node:
            m_thumb = node.getElementsByTagName("gco:CharacterString")[0]
            if m_thumb.childNodes.length > 0:

                m_thumb_url = m_thumb.childNodes[0].nodeValue
                # print(m_thumb_url, len(m_thumb_url))


            else:
                m_thumb_url = "N/A"

        return (meta_thumbname.append(m_thumb_url),
                meta_id.append(ID), meta_uuid.append(UUID))

    except:
        print("Erron in " + str(UUID) + " : " + str(ID))


with open('SearchList.csv', 'r') as f:
    spamreader = csv.reader(f, delimiter=' ', quotechar='|')
    for row in spamreader:
        output = (', '.join(row))
        ID = output.split(',')[0]
        UUID = output.split(",")[1]
        # print (ID + " : " + UUID)
        get_thumb(ID, UUID)

# for r in zip(meta_id, meta_uuid, meta_thumbname):
#
#     if r[2] != "N/A" and len(r[2]) < 60 and r[2] !='':
#         print(r)

with open("GN_t_thumb_url.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for r in zip(meta_id, meta_uuid, meta_thumbname):

        if r[2] != "N/A" and len(r[2]) < 60 and r[2] !='':
            writer.writerow(r)

        # if r != "N/A" and len(r) < 60:
        #     print(r)
