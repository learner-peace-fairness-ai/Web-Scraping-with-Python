import requests
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now().timestamp())


def get_links(articuleUrl):
    url = f'https://en.wikipedia.org{articuleUrl}'
    
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    return soup.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = get_links('/wiki/Kevin_Bacon')
while len(links) > 0:
    link = links[random.randint(0, len(links)-1)]
    newArticle = link['href']
    print(newArticle)

    links = get_links(newArticle)
