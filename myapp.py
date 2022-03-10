from dash import dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
import pandas as pd
# Make FIPS string so it can be read properly and avoid holes
colors = {"background": "#111111", "text": "#7FDBFF"}
df = pd.read_csv('updated-census-tract.csv',  dtype={"FIPS": str})
df2 = pd.read_csv('urbanization-state.csv')
df2.columns = map(str.strip, df2.columns)
df2['ab'] = df2['ab'].apply(str.strip)
df2['urbanindex'] = df2['urbanindex'].astype(float)

countymap = px.choropleth_mapbox(df, title='most urban counties',  template='plotly_dark', geojson=counties, locations='FIPS', color='urbanindex',
                           color_continuous_scale="Viridis",
                           range_color=(0, 14),
                           mapbox_style="carto-darkmatter",
                           zoom=3, center={"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           hover_data=['total_pop'],
                           labels={'urbanindex': 'urban index', 'total_pop': 'total population'}
                           )
countymap.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})


statemap = go.Figure(data=go.Choropleth(
    locations=df2['ab'],  # Spatial coordinates
    z=df2['urbanindex'].astype(float),  # Data to be color-coded
    locationmode='USA-states',  # set of locations match entries in `locations`
    colorscale='Reds',
    autocolorscale=False,
    marker_line_color='white',
    colorbar_title="urbanization index",

))

statemap.update_layout(
    


    geo=dict(
        bgcolor= 'rgba(0,0,0,0)', lakecolor='#000000',
                                          landcolor='rgba(51,17,0,0.2)',
                                          subunitcolor='black',
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=True,  # lakes
        ),
        title_text='Which States are the Most Urban?',
        font = {"size": 9, "color":"White"},
        titlefont = {"size": 15, "color":"White"},
        margin={"r": 0, "t": 40, "l": 0, "b": 0},
        paper_bgcolor='#000000',
        plot_bgcolor='#000000',
),
app=dash.Dash(__name__)
figures=["County Map", "State Map"]
app.layout=html.Div(
    style={"backgroundColor": colors["background"]},
    children=[
        html.H1(
            children="Maps showing how rural or urban an area is",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        html.Div(
            children="""
        Multiple graphs
    """,
            style={"textAlign": "center", "color": colors["text"]},
        ),
        dcc.Graph(
            id="plot",
            style={'width': '100', 'height': '90vh'}

        ),
        dcc.Dropdown(
            id="variables",
            options=[{"label": i, "value": i} for i in figures],
            value=figures[0],
            searchable=False,
            clearable=False,
            style={'display': 'inline-block','width': '40%'}
        ),

    ],
)





@ app.callback(Output("plot", "figure"), [Input("variables", "value")])
def update_graph(fig_name):

    if fig_name == "State Map":
        return statemap

    if fig_name == "County Map":
        return countymap
# Turn off reloader if inside Jupyter
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
