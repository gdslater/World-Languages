from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://en.wikipedia.org/wiki/List_of_official_languages_by_country_and_territory'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
# encode('utf-8') ignores special characters that python can't read.
#print(soup.encode("utf-8"))

table = soup.find('table', {'class':'wikitable sortable'}).tbody
print(table.encode("utf-8"))

#rows = table.find_all('tr')
#columns = [v.text for v in rows[0].find_all('td')]