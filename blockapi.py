import numpy as np
import urllib
import json
import requests
import urllib.request
import pandas as pd
from rich.progress import track 
results = []
df = pd.read_csv('urbanization-census-tract.csv')
lat = df['lat_tract'].astype(float)
lon = df['long_tract'].astype(float)
for i in track(range(1, 2)): #iterate each row for API
    
    row = df.iloc[i]
# Encode parameters
    params = urllib.parse.urlencode(
    {'latitude': row['lat_tract'], 'longitude': row['long_tract'], 'format': 'json'})
    # Contruct request URL
    url = 'https://geo.fcc.gov/api/census/block/find?' + params

# Get response from API
    response = requests.get(url)

    # Parse json in response
    data = response.json()
    results.append(data['County']['FIPS'])
    breakpoint()

# Print FIPS code


df['FIPS'] = np.array(data)

df.to_csv('urbanization-census-tract-updated', sep='\t')