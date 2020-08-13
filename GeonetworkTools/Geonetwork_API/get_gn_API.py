import requests
import xml.etree.ElementTree as ET

host = 'localhost'
uuid = 'd14414d0-a356-4843-8bbb-ebcbb6630017'
auth = ('Samir', 'Ge0ne!RDS')
api = 'geonetwork3102/srv/api/0.1/records/'

headers = {
    'accept': 'application/xml',
    'X-XSRF-TOKEN': 'd73a1bef-cb21-4f73-8f5f-4bc0e836c623',
}

response = requests.get('http://' + host + ':8080/' + api + uuid, auth=auth, headers=headers)
print(response.text)
