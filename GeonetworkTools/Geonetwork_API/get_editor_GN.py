import requests
import json

auth = ('Samir', 'Ge0ne!RDS')

headers = {
    'accept': 'application/xml',
    'X-XSRF-TOKEN': '5463bcf8-7841-46d9-8cae-c3e3851cbbbb',
}

params = (
    ('metadataType', 'METADATA'),
    ('uuidProcessing', 'OVERWRITE'),
    ('group', 'dummy'),
    ('category', 'datasets'),
    ('rejectIfInvalid', 'false'),
    ('publishToAll', 'false'),
    ('assignToCatalog', 'false'),
    ('transformWith', '_none_'),
)

data = {
  'file': '[object File]'
}
response = requests.get(
    'http://localhost:8080/geonetwork3102/srv/api/0.1/records/31541eb3-15bd-438d-8049-fc85cf57e09a/editor',
    headers=headers, params=params)

print(response.status_code)
