from urllib.request import urlopen
import ssl
import certifi
from bs4 import BeautifulSoup
import re

context = ssl.create_default_context(cafile=certifi.where())
html = urlopen(
    'https://pythonscraping.com/pages/page3.html', context=context)
bsObj = BeautifulSoup(html, 'html.parser')

tag_list = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
print(len(tag_list))
