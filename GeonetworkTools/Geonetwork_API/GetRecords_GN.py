import requests
from rdflib import Graph

g = Graph()
headers = {
    'accept': '*/*',
    'X-XSRF-TOKEN': 'f6cf54bd-0ebf-4f0d-b1e6-ebcf815723fe',
}

params = (
    ('from', '1'),
    ('hitsPerPage', '10'),
    ('title', 'Land Cover of Greater Chittagong, Bangladesh 2010'),
    ('similarity', '0.8'),
)

# response = requests.get('http://localhost:8080/geonetwork3102/srv/api/0.1/records', headers=headers, params=params)
g.parse('http://localhost:8080/geonetwork3102/srv/api/0.1/records', headers=headers, params=params)

for index, (sub, pred, obj) in enumerate(g):
    print(index, sub)

    if index == 20:
        break