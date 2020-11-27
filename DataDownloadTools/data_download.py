import requests
import json
import pandas as pd

payload = {'user': 'user1', 'password': 'password'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

url = "http://h-web01.nve.no/chartserver/ShowData.aspx?req=getchart&ver=1.0&time=-3;" \
      "0&chd=ds=htsr,da=29,id=1977.1.3.17.1,rt=0&mth=inst&vfmt=json"

r = requests.get(url, headers=headers)

js = json.loads(r.text)

# print(json.dumps(js, indent=2))


def timestamp_conversion(t_date):
    c_time = (int(t_date.strip('/Date()'))) / 1000
    c_datetime = pd.Timestamp(c_time, unit='s')
    return c_datetime


for d in js:
    print(d["LegendText"])
    for data in d['SeriesPoints']:
        print(timestamp_conversion(data['Key']), data['Value'], data['CorrectionMark'])

