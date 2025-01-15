import requests
from bs4 import BeautifulSoup

URL = 'https://pythonscraping.com/pages/page3.html'

response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

tag_list = soup.findAll(lambda tag: len(tag.attrs) == 2)
print(len(tag_list))
