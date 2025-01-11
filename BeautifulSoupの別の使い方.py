from urllib.request import urlopen
import ssl
import certifi
from bs4 import BeautifulSoup

context = ssl.create_default_context(cafile=certifi.where())
html = urlopen(
    'https://pythonscraping.com/pages/warandpeace.html', context=context)
bsObj = BeautifulSoup(html, 'html.parser')

nameList = bsObj.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())
