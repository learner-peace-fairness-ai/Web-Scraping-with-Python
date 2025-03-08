import random
import re
import sqlite3
import time

import requests
from bs4 import BeautifulSoup

WAIT_SEC = 1


def store(title, content):
    with sqlite3.connect('scraping') as con:
        con.execute('INSERT INTO pages (title, content) VALUES (?, ?)', (title, content))
    

def get_links(article_url):
    response = requests.get(f'https://en.wikipedia.org{article_url}')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('h1').get_text()
    content = soup.select_one('#mw-content-text p:not([class=mw-empty-elt])').get_text()
    
    store(title, content)
    body_content = soup.select_one('#bodyContent')
    return body_content.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = get_links('/wiki/Kevin_Bacon')
for i in range(2):
    new_article = random.choice(links).attrs['href']
    print(new_article)

    time.sleep(WAIT_SEC)

    links = get_links(new_article)
