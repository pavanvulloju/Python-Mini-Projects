# Opens the first result of the google search results
# I'm Feeling Lucky on Google.com

import webbrowser
import requests
from bs4 import BeautifulSoup

query = input('Enter google search query: ')
query = query.replace(' ', '+')
url = 'https://www.google.com/search?q=' + query + '&btnI=Im+Feeling+Lucky'
r = requests.get(url)
if r.status_code == 200:
	soup = BeautifulSoup(r.text, 'lxml')
	first_link = soup.find('a').get('href')
	webbrowser.open(first_link)
else:
	print('Error Fetching the result')
