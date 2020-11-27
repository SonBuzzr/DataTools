import requests
import json
import xml.etree.ElementTree as ET

host = 'localhost'
uuid = 'd14414d0-a356-4843-8bbb-ebcbb6630017'
auth = ('Samir', 'Ge0ne!RDS')
api = 'geonetwork3102/srv/api/0.1/records/'
get_group = 'geonetwork3102/srv/api/0.1/groups/'
batch_editing = 'geonetwork3102/srv/api/0.1/records/batchediting'

headers = {
    'accept': 'application/json',
    'X-XSRF-TOKEN': 'fb4f50f3-db37-48d8-b77c-ab314cb248b0'
}

params = (
    ('uuids', 'd14414d0-a356-4843-8bbb-ebcbb6630017'),
    ('updateDateStamp', 'false'),
)

data = '[ { "condition": "Hello", "value": "Land cover of Nepal 2010 Updated", "xpath": ' \
       '"/gmd:MD_Metadata/gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/' \
       'gmd:CI_Citation/gmd:title/gco:CharacterString" }]'

# response = requests.get('http://' + host + ':8080/' + api + uuid, auth=auth, headers=headers)
response = requests.put('http://' + host + ':8080/' + batch_editing, auth=auth, headers=headers, params=params, data=data)


print(response.text)