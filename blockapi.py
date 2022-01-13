import urllib
import json
import requests
import urllib.request
import pandas as pd

df = pd.read_csv('urbanization-census-tract.csv')
latitude = df['lat_tract']
longitude = df['long_tract']

with urllib.request.urlopen("https://geo.fcc.gov/api/census/block/find?latitude=32.47718&longitude=-86.49007&format=json") as url:
    data = json.loads(url.read().decode())
    print(data)

print(json.dumps(data, indent=4, sort_keys=True))

print(data['results'][0]['state_fips'])
print(data['results'][0]['county_fips'])
print(data['results'][0]['county_name'])
