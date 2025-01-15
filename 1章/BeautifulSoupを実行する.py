import requests
from bs4 import BeautifulSoup

URL = 'https://pythonscraping.com/pages/page1.html'

response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
print(soup.h1)
