from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup
import requests

response = requests.get('https://pythonscraping.com')
html = response.text

soup = BeautifulSoup(html, 'html.parser')
img = soup.find('img', {'alt': 'python-logo'})
src_url = img['src']

img_response = requests.get(src_url)
file_extension = Path(urlparse(src_url).path).suffix
with open(f'logo{file_extension}', 'wb') as fw:
    for chunk in img_response.iter_content(chunk_size=100000):
        fw.write(chunk)
