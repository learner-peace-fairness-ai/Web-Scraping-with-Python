from urllib.request import urlopen
import ssl
import certifi
from bs4 import BeautifulSoup
import re

context = ssl.create_default_context(cafile=certifi.where())
html = urlopen(
    'https://pythonscraping.com/pages/page3.html', context=context)
bsObj = BeautifulSoup(html, 'html.parser')

images = bsObj.findAll(
    'img', {'src': re.compile('\.\./img/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])
