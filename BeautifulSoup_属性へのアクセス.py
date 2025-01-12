from urllib.request import urlopen
import ssl
import certifi
from bs4 import BeautifulSoup
import re

context = ssl.create_default_context(cafile=certifi.where())
html = urlopen(
    'https://pythonscraping.com/pages/page3.html', context=context)
bsObj = BeautifulSoup(html, 'html.parser')

image = bsObj.find(
    'img', {'src': re.compile('\.\./img/gifts/img.*\.jpg')})

print(image.attrs['src'])

print(image['src'])
