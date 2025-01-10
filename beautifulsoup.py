from urllib.request import urlopen
import ssl
import certifi
from bs4 import BeautifulSoup

context = ssl.create_default_context(cafile=certifi.where())
html = urlopen('https://pythonscraping.com/pages/page1.html', context=context)

bsObj = BeautifulSoup(html.read(), 'html.parser')
print(bsObj.h1)
