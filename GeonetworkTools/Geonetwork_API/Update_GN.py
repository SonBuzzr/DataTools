import requests

auth = ('Samir', 'Ge0ne!RDS')

headers = {
    'accept': 'application/xml',
    'X-XSRF-TOKEN': '83693447-09af-4aeb-847e-1036e91f92e6',
}

params = (
    ('metadataType', 'METADATA'),
    ('uuidProcessing', 'OVERWRITE'),
    ('rejectIfInvalid', 'false'),
    ('publishToAll', 'false'),
    ('assignToCatalog', 'false'),
    ('transformWith', '_none_'),
)

get_API = 'http://localhost:8080/geonetwork3102/srv/api/0.1/records/d14414d0-a356-4843-8bbb-ebcbb6630017'
update_API = 'http://localhost:8080/geonetwork3102/srv/api/0.1/records?'

get_response = requests.get(get_API, headers=headers)
# print(get_response.text)

data = get_response.text

update_response = requests.post(update_API, auth=auth, headers=headers, params=params, data=data)

print(update_response.status_code)