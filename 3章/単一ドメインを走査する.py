import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Kevin_Bacon'

response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

for link in soup.findAll('a'):
    if 'href' in link.attrs:
        print(link['href'])
