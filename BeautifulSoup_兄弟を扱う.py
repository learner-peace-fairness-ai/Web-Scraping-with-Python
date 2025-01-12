from urllib.request import urlopen
import ssl
import certifi
from bs4 import BeautifulSoup

context = ssl.create_default_context(cafile=certifi.where())
html = urlopen(
    'https://pythonscraping.com/pages/page3.html', context=context)
bsObj = BeautifulSoup(html, 'html.parser')

for sibling in bsObj.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)
