import requests
from requests.auth import HTTPBasicAuth

auth = ('Samir', 'Ge0ne!RDS')

headers = {
    'accept': 'application/xml',
    'X-XSRF-TOKEN': 'fb4f50f3-db37-48d8-b77c-ab314cb248b0',
}

headers1 = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'X-XSRF-TOKEN': '5463bcf8-7841-46d9-8cae-c3e3851cbbbb',
}
params = (
    ('metadataType', 'METADATA'),
    ('uuidProcessing', 'OVERWRITE'),
    ('category', 'datasets'),
    ('rejectIfInvalid', 'false'),
    ('publishToAll', 'true'),
    ('assignToCatalog', 'false'),
    ('transformWith', '_none_'),
)
response = requests.get('http://localhost:8080/geonetwork3102/srv/api/0.1/records/31541eb3-15bd-438d-8049-fc85cf57e09a',
                        auth=auth, headers=headers)

xml = response.text
print(xml)

response = requests.post('http://localhost:8080/geonetwork3102/srv/api/0.1/records', auth=auth, headers=headers1,
                         params=params,
                         data=xml)
print(response.content)
