import requests
import json

host = 'localhost'
auth = ('Samir', 'Ge0ne!RDS')

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

params = {'any': 'hkh',
          'type': 'dataset',
          '_content_type': 'json',
          'fast': 'index',
          'from': 1,
          'resultType': 'details',
          'to': 100}

api = 'http://localhost:8080/geonetwork3102/srv/eng/q?'

search_request = requests.get(api, headers=headers, params=params)

metadata_result = json.loads(search_request.text)

print(type(metadata_result['metadata']))
# print(metadata_result)

count = 0
# loop through multiple metadata
# for single metadata it doesn't work
for meta_data in metadata_result['metadata']:

    if 'image' not in meta_data:
        print('*** Thumbnail Not Found ***', '\n')
        continue

    if len(meta_data['image'][0]) < 60:
        print(meta_data['title'])
        print(meta_data['geonet:info']['id'], meta_data['geonet:info']['uuid'])
        print(meta_data['image'][0], len(meta_data['image'][0]), '\n')
        count += 1

print('Total Metadata:', count)
