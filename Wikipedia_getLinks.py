from urllib.request import urlopen
import ssl
import certifi
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now().timestamp())


def getLinks(articuleUrl):
    context = ssl.create_default_context(cafile=certifi.where())
    html = urlopen(
        f'https://en.wikipedia.org{articuleUrl}', context=context)
    bsObj = BeautifulSoup(html, 'html.parser')

    return bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    link = links[random.randint(0, len(links)-1)]
    newArticle = link['href']
    print(newArticle)

    links = getLinks(newArticle)
