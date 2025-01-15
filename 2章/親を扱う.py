import requests
from bs4 import BeautifulSoup

URL = 'https://pythonscraping.com/pages/page3.html'

response = requests.get(URL)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

tag = soup.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling
print(tag.get_text())
