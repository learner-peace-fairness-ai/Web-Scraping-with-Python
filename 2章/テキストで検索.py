import requests
from bs4 import BeautifulSoup

URL = 'https://pythonscraping.com/pages/warandpeace.html'

response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

nameList = soup.findAll(string='the prince')
print(len(nameList))
