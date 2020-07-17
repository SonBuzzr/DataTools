import requests

headers = {
    'accept': 'application/json',
    'X-XSRF-TOKEN': 'b98f7620-1488-4521-8bba-0b21f9eadf2a',
}

response = requests.get('http://localhost:8080/geonetwork3102/srv/api/0.1/groups/5', headers=headers)
print(response.content)