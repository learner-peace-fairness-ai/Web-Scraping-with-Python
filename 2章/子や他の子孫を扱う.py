import requests
from bs4 import BeautifulSoup

URL = 'https://pythonscraping.com/pages/page3.html'

response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

for child in soup.find('table', {'id': 'giftList'}).children:
    print(child)
