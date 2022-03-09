
import plotly.express as px
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
import pandas as pd
df = pd.read_csv('updated-census-tract.csv',  dtype={"FIPS": str}) #Make FIPS string so it can be read properly and avoid holes 

import plotly.express as px

fig = px.choropleth_mapbox(df, title = 'most urban counties',  template='plotly_dark', geojson=counties, locations='FIPS', color='urbanindex',
                           color_continuous_scale="Viridis",
                           range_color=(0, 14),
                           mapbox_style="carto-darkmatter",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           hover_data=  ['total_pop'],
                           labels={'urbanindex':'urban index'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()