import plotly.express as px
import plotly
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from urllib.request import urlopen
import json

df = pd.read_csv('language_data.csv')

with urlopen('https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson') as response:
    geojson_countries = json.load(response)

#app = dash.Dash(__name__)
#server = app.server
px.set_mapbox_access_token(open(".mapbox_token.txt").read())

df['Value'] = 1

fig = px.choropleth_mapbox(df,geojson=geojson_countries, featureidkey='properties.ADMIN', locations=df.Country, height=800, width=1200,
			mapbox_style='light', zoom=1, opacity=.5)
#app.layout = html.Div(children=[
#	dcc.Graph()
#]

fig.update_layout()

#fig.show()
plotly.offline.plot(fig)

#if __name__ == '__main__':
 #   app.run_server(debug=True)