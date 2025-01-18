import re

import requests
from bs4 import BeautifulSoup

URL = 'https://pythonscraping.com/pages/page3.html'

response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

img = soup.find('img', {'src': re.compile('\.\./img/gifts/img.*\.jpg')})

print(img.attrs['src'])
print(img['src'])
