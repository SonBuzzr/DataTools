# List all the DOI using Datacite REST API

import requests
import json

import CSV_Read_Write

url = "https://api.datacite.org/dois"
outputFile = 'DataciteDOI.csv'

querystring = {"client-id": "icimod.rds", "page[size]": "400"}

headers = {'accept': 'application/vnd.api+json'}

doiLink = []
rdsUrl = []
doiIden = []
mtitle = []

r = requests.get(url, headers=headers, params=querystring)
res = r.json()
count = 0

for links in res['data']:
    count += 1
    # for doi in links['attributes']['identifiers']:

    for doi, title in zip(links['attributes']['identifiers'], links['attributes']['titles']):
        # print(doi['identifier'], links['attributes']['url'], links['attributes']['doi'], title['title'])
        link = doi['identifier']
        durl = links['attributes']['url']
        diden = links['attributes']['doi']
        ttl = title['title']

        doiLink.append(link)
        rdsUrl.append(durl)
        doiIden.append(diden)
        mtitle.append(ttl)

print("No. of DOI: {}".format(count))

heading = {'DOI': doiLink, 'URL': rdsUrl, 'Identifier': doiIden, 'Title': mtitle}
CSV_Read_Write.writeCSV_pd(outputFile, **heading)