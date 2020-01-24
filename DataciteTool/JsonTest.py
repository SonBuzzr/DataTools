import requests
import json

with open('example_2.json') as f:
    jsonFile = json.load(f)

    for v in jsonFile['data']:
        print(v['attributes']['url'])

        # for i in v['attributes']['identifiers']:
        #     print(i['identifier'])

        for doi, title in zip(v['attributes']['identifiers'], v['attributes']['titles']):
            print(doi['identifier'], title['title'])
# r = requests.get("https://support.oneskyapp.com/hc/en-us/article_attachments/202761727/example_2.json")
# res = r.json()

# Extract specific node content.
# print(res['quiz']['sport'])

# Dump data as string
# data = json.dumps(res)
# print(data)
