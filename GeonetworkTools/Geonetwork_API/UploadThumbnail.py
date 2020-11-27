import requests
import json

host = 'localhost'
auth = ('Samir', 'Ge0ne!RDS')

headers = {
    'accept': 'application/json',
    'authorization': 'Basic U2FtaXI6R2UwbmUhUkRT',
    'Content-Type': 'application/json',
    'X-XSRF-TOKEN': 'fb4f50f3-db37-48d8-b77c-ab314cb248b0',
}

data = '{ "logo": null, "website": null, "defaultCategory": null, "allowedCategories": [], "enableAllowedCategories": ' \
       'false, "name": "dummy", "id": 13, "description": "error ehehssdfsdfod metadata"}'

params = {'visibility': 'public',
          'url': 'http://192.168.10.77:8080/geonetwork/srv/api/records/f36d4ba6-77db-4c7a-904e-1c6d7de673fa/attachments/PPT_05.png',
          'approved': 'true',
          }

response = requests.put('http://localhost:8080/geonetwork3102/srv/api/0.1/groups/13', auth=auth, headers=headers, data=data)

print(response.status_code)
