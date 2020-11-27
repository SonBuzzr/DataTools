import pandas as pd
from pandas.io.json import json_normalize

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
url = "http://h-web01.nve.no/chartserver/ShowData.aspx?req=getchart&ver=1.0&time=-3;" \
      "0&chd=ds=htsr,da=29,id=1977.1.3.17.1,rt=0&mth=inst&vfmt=json"

df = pd.read_json(url)
station_name = pd.DataFrame(df.LegendText.values.tolist())
print(station_name)
station_data = pd.DataFrame(df.SeriesPoints.values.tolist())
print(pd.DataFrame.from_records(station_data).head(5))

