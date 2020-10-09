import plotly.express as px
import plotly
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from urllib.request import urlopen
import json

df = pd.read_csv('language_data.csv')

# Geojson (the country borders for the choropleth map)
with urlopen('https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson') as response:
    geojson_countries = json.load(response)

app = dash.Dash(__name__)
server = app.server
px.set_mapbox_access_token(open(".mapbox_token.txt").read())

df['Value'] = 1

languages_list = [{'label': 'English', 'value': 'English'},
	        	{'label': 'French', 'value': 'French'},
	        	{'label': 'Russian', 'value': 'Russian'},
	        	{'label': 'Albanian', 'value': 'Albanian'},
	        	{'label': 'Italian', 'value': 'Italian'},
	        	{'label': 'Arabic', 'value': 'Arabic'},
	        	{'label': 'Tamazight', 'value': 'Tamazight'},
	        	{'label': 'Catalan', 'value': 'Catalan'},
	        	{'label': 'Spanish', 'value': 'Spanish'},
	        	{'label': 'Portuguese', 'value': 'Portuguese'},
	        	{'label': 'Kimbundu', 'value': 'Kimbundu'},
	        	{'label': 'Umbundu', 'value': 'Umbundu'},
	        	{'label': 'Kikongo', 'value': 'Kikongo'},
	        	{'label': 'Chokwe', 'value': 'Chokwe'},
	        	{'label': 'Kwanyama', 'value': 'Kwanyama'},
	        	{'label': 'Armenian', 'value': 'Armenian'},
	        	{'label': 'Pashto', 'value': 'Pashto'},
	        	{'label': 'Dari', 'value': 'Dari'},
	        	{'label': 'German', 'value': 'German'},
	        	{'label': 'Azerbaijani', 'value': 'Azerbaijani'},
	        	{'label': 'Bengali', 'value': 'Bengali'},
	        	{'label': 'Belarusian', 'value': 'Belarusian'},
	        	{'label': 'Dutch', 'value': 'Dutch'},
	        	{'label': 'Dzongkha', 'value': 'Dzongkha'},
	        	{'label': 'Bosnian', 'value': 'Bosnian'},
	        	{'label': 'Serbian', 'value': 'Serbian'},
	        	{'label': 'Tswana', 'value': 'Tswana'},
	        	{'label': 'Bulgarian', 'value': 'Bulgarian'},
	        	{'label': 'Kirundi', 'value': 'Kirundi'},
	        	{'label': 'Swahili', 'value': 'Swahili'},
	        	{'label': 'Khmer', 'value': 'Khmer'},
	        	{'label': 'Mandarin', 'value': 'Mandarin'},
	        	{'label': 'Comorian', 'value': 'Comorian'},
	        	{'label': 'Croatian', 'value': 'Croatian'},
	        	{'label': 'Greek', 'value': 'Greek'},
	        	{'label': 'Turkish', 'value': 'Turkish'},
	        	{'label': 'Czech', 'value': 'Czech'},
	        	{'label': 'Slovak', 'value': 'Slovak'},
	        	{'label': 'Danish', 'value': 'Danish'},
	        	{'label': 'Tetum', 'value': 'Tetum'},
	        	{'label': 'Quechua', 'value': 'Quechua'},
	        	{'label': 'Tigrinya', 'value': 'Tigrinya'},
	        	{'label': 'Estonian', 'value': 'Estonian'},
	        	{'label': 'Swazi', 'value': 'Swazi'},
	        	{'label': 'Amharic', 'value': 'Amharic'},
	        	{'label': 'Fijian', 'value': 'Fijian'},
	        	{'label': 'Fiji Hindi', 'value': 'Fiji Hindi'},
	        	{'label': 'Finnish', 'value': 'Finnish'},
	        	{'label': 'Swedish', 'value': 'Swedish'},
	        	{'label': 'Georgian', 'value': 'Georgian'},
	        	{'label': 'Greenlandic', 'value': 'Greenlandic'},
	        	{'label': 'Fula', 'value': 'Fula'},
	        	{'label': 'Hungarian', 'value': 'Hungarian'},
	        	{'label': 'Icelandic', 'value': 'Icelandic'},
	        	{'label': 'Hindi', 'value': 'Hindi'},
	        	{'label': 'Indonesian', 'value': 'Indonesian'},
	        	{'label': 'Javanese', 'value': 'Javanese'},
	        	{'label': 'Sundanese', 'value': 'Sundanese'},
	        	{'label': 'Madurese', 'value': 'Madurese'},
	        	{'label': 'Persian', 'value': 'Persian'},
	        	{'label': 'Irish', 'value': 'Irish'},
	        	{'label': 'Hebrew', 'value': 'Hebrew'},
	        	{'label': 'Japanese', 'value': 'Japanese'},
	        	{'label': 'Kazakh', 'value': 'Kazakh'},
	        	{'label': 'Korean', 'value': 'Korean'},
	        	{'label': 'Kyrgyz', 'value': 'Kyrgyz'},
	        	{'label': 'Lao', 'value': 'Lao'},
	        	{'label': 'Latvian', 'value': 'Latvian'},
	        	{'label': 'Sotho', 'value': 'Sotho'},
	        	{'label': 'Lithuanian', 'value': 'Lithuanian'},
	        	{'label': 'Luxembourgish', 'value': 'Luxembourgish'},
	        	{'label': 'Malagasy', 'value': 'Malagasy'},
	        	{'label': 'Malay', 'value': 'Malay'},
	        	{'label': 'Dhivehi', 'value': 'Dhivehi'},
	        	{'label': 'Maltese', 'value': 'Maltese'},
	        	{'label': 'Woleaian', 'value': 'Woleaian'},
	        	{'label': 'Mongolian', 'value': 'Mongolian'},
	        	{'label': 'Burmese', 'value': 'Burmese'},
	        	{'label': 'Nauruan', 'value': 'Nauruan'},
	        	{'label': 'Nepali', 'value': 'Nepali'},
	        	{'label': 'Maori', 'value': 'Maori'},
	        	{'label': 'Macedonian', 'value': 'Macedonian'},
	        	{'label': 'Norwegian', 'value': 'Norwegian'},
	        	{'label': 'Sami', 'value': 'Sami'},
	        	{'label': 'Urdu', 'value': 'Urdu'},
	        	{'label': 'Palauan', 'value': 'Palauan'},
	        	{'label': 'Punjabi', 'value': 'Punjabi'},
	        	{'label': 'Aymara', 'value': 'Aymara'},
	        	{'label': 'Hiri Motu', 'value': 'Hiri Motu'},
	        	{'label': 'Tok Pisin', 'value': 'Tok Pisin'},
	        	{'label': 'Filipino', 'value': 'Filipino'},
	        	{'label': 'Polish', 'value': 'Polish'},
	        	{'label': 'Romanian', 'value': 'Romanian'},
	        	{'label': 'Kinyarwanda', 'value': 'Kinyarwanda'},
	        	{'label': 'Tamil', 'value': 'Tamil'},
	        	{'label': 'Slovene', 'value': 'Slovene'},
	        	{'label': 'Afrikaans', 'value': 'Afrikaans'},
	        	{'label': 'Sinhala', 'value': 'Sinhala'},
	        	{'label': 'Thai', 'value': 'Thai'},
	        	{'label': 'Vietnamese', 'value': 'Vietnamese'},
	        	{'label': 'Turkmen', 'value': 'Turkmen'},
	        	{'label': 'Ukrainian', 'value': 'Ukrainian'},
	        	{'label': 'Uzbek', 'value': 'Uzbek'},
	        	{'label': 'Shona', 'value': 'Shona'},
	        	{'label': 'Ndebele', 'value': 'Ndebele'},
	        	{'label': 'Zulu', 'value': 'Zulu'},
	        	{'label': 'Xhosa', 'value': 'Xhosa'},
	        	{'label': 'Tsonga', 'value': 'Tsonga'}]

languages_list = sorted(languages_list, key = lambda i: (i['label']))

app.layout = html.Div([

	# Header
	html.Div([

	]),

	# Right side Div
	html.Div([
		dcc.Dropdown(id='selected_languages',
			options = languages_list,
			multi = True,
			value = "",
			placeholder="Search for a Language"
		)
	]),

	# Left side Div
	html.Div([
		dcc.Graph(id='map')
	]),

	# Footer
	html.Div([

	]),
])

@app.callback(
    dash.dependencies.Output('map', 'figure'),
    [dash.dependencies.Input('selected_languages', 'value')])

def update_map(languages):
	# languages is a list of the languages selected:
	new_df = pd.DataFrame(columns=df.columns)
	new_df = new_df.fillna(0)
	for lang in languages:
		df1 = df[df['Official language'].str.contains(lang)]
	df2 = df[df['Widely spoken'].str.contains(lang)]
	result = df1.append(df2)
	new_df = new_df.append(result)

	fig = px.choropleth_mapbox(new_df,geojson=geojson_countries, featureidkey='properties.ADMIN', locations=new_df.Country,
		height=800, width=1200, mapbox_style='light', zoom=1, opacity=.5)
	return fig

#fig.show()
#plotly.offline.plot(fig)

if __name__ == '__main__':
	app.run_server(debug=True)