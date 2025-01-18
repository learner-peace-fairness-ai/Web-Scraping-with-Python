import re

import requests
from bs4 import BeautifulSoup

URL = 'https://pythonscraping.com/pages/page3.html'

response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

images = soup.findAll('img', {'src': re.compile('\.\./img/gifts/img.*\.jpg')})
for img in images:
    print(img['src'])
