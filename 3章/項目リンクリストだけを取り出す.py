import requests
from bs4 import BeautifulSoup
import re

URL = 'https://en.wikipedia.org/wiki/Kevin_Bacon'

response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

item_links = soup.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
for link in item_links:
    if 'href' in link.attrs:
        print(link['href'])
