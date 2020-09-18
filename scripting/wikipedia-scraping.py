from bs4 import BeautifulSoup
import requests
import pandas as pd

# NOTE:
# Wikipedia has a resource for scripting data from tables but I want to challenge myself by webscraping it myself :)

URL = 'https://en.wikipedia.org/wiki/List_of_official_languages_by_country_and_territory'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
# encode('utf-8') ignores special characters that python can't read.
#print(soup.encode("utf-8"))

table = soup.find('table', {'class':'wikitable sortable'}).tbody
#print(table.encode("utf-8"))

rows = table.find_all('tr')
#print(rows[1].encode("utf-8"))

headers = [c.text.replace('\n', '') for c in rows[0].find_all('th')]

# TO DO: get flag urls to make app look prettier
# headers.insert(1, 'Flag')

df = pd.DataFrame(columns=headers)

def format_string(s):
	return s.replace('[a]', '').replace('[b]', '').replace('[c]', '').replace('[d]', '').replace('[e]', '').replace('[f]', '').replace('[g]', '').replace('[h]', '').replace('[1]', '').replace('[2]','').replace('[3]', '').replace('[4]', '').replace('[5]', '').replace('[6]', '').replace('[7]', '').replace('[8]', '').replace('[9]', '').replace('[10]', '').replace('[11]', '').replace('[12]', '').replace('[13]', '').replace('[14]', '').replace('[15]', '').replace('[16]', '').replace('[17]', '').replace('[18]', '').replace('[19]', '').replace('[20]', '').replace('[21]', '').replace('[22]', '').replace('[23]', '').replace('[24]', '').replace('[25]', '').replace('[26]', '').replace('[27]', '').replace('[28]', '').replace('[29]', '').replace('[30]', '').replace('[31]', '').replace('[32]', '').replace('[33]', '').replace('[34]', '').replace('[35]', '').replace('[36]', '').replace('[37]', '').replace('[38]', '').replace('[39]', '').replace('[40]', '').replace('[41]', '').replace('[42]', '').replace('[43]', '').replace('[44]', '').replace('[45]', '').replace('[46]', '').replace('[47]', '').replace('[48]', '').replace('[49]', '').replace('[50]', '').replace('[51]', '').replace('[52]', '').replace('[53]', '').replace('[54]', '').replace('[55]', '').replace('[56]', '').replace('[57]', '').replace('[58]', '').replace('[59]', '').replace('[60]', '').replace('[61]', '').replace('[63]', '').replace('[64]', '').replace('[65]', '').replace('[66]', '').replace('[67]', '').replace('[68]', '').replace('[69]', '').replace('[70]', '').replace('[71]', '').replace('[72]', '').replace('[citation needed]', '')

for i in range(1, len(rows)):
	tds = rows[i].find_all('td')
	if tds:
		values = [td.text for td in tds]
		### Cleaning data to be in more desirable format (basically removing /n and [#])
		for i in range(0, 6):
			values[i] = values[i].strip()
			values[i] = values[i].strip('\n')
			values[i] = format_string(values[i])
			if i != 0:
				values[i] = values[i].split('\n')
			### Comment this out for empty list instead of 'None'
			if values[i] == ['']:
				values[i] = 'None'
			###
	df = df.append(pd.Series(values, index=headers), ignore_index=True)

## Data Frame Print Options ##
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
#print(df['Minority language'])

df.to_csv('C:/Users/golda/Desktop/python/world-languages-map/language_data.csv', index=False)
