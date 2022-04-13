import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('urbanization-state.csv')
df.columns = map(str.strip, df.columns)
df['ab'] = df['ab'].apply(str.strip)
df['urbanindex'] = df['urbanindex'].astype(float)

fig = go.Figure(data=go.Choropleth(
    locations=df['ab'],  # Spatial coordinates
    z=df['urbanindex'].astype(float),  # Data to be color-coded
    locationmode='USA-states',  # set of locations match entries in `locations`
    colorscale='Reds',
    autocolorscale=False,
    marker_line_color='white',
    colorbar_title="urbanization index",
))

fig.update_layout(
    title_text='Which States are the Most Urban?',

    geo=dict(
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=True,  # lakes
        lakecolor='rgb(255, 255, 255)'),
),


fig.show()
