
import plotly.express as px

import pandas as pd
df = pd.read_csv('urbanization-census-tract.csv')

fig = px.scatter_geo(df,  lon='long_tract', lat='lat_tract', color='urbanindex',
                     hover_name='state',
                     hover_data=['population'],
                     scope="usa",
                           labels={'Urban': 'urban index'}
                     )
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
