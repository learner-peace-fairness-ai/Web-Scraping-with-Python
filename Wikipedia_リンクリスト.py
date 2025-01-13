from urllib.request import urlopen
import ssl
import certifi
from bs4 import BeautifulSoup

context = ssl.create_default_context(cafile=certifi.where())
html = urlopen(
    'https://en.wikipedia.org/wiki/Kevin_Bacon', context=context)
bsObj = BeautifulSoup(html, 'html.parser')

for link in bsObj.findAll('a'):
    if 'href' in link.attrs:
        print(link['href'])
