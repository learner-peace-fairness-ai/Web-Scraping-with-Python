from urllib.request import urlopen
import ssl
import certifi
from bs4 import BeautifulSoup

context = ssl.create_default_context(cafile=certifi.where())
html = urlopen(
    'https://pythonscraping.com/pages/page3.html', context=context)
bsObj = BeautifulSoup(html, 'html.parser')

print(bsObj.find('img', {'src': '../img/gifts/img1.jpg'}
                 ).parent.previous_sibling.get_text())
