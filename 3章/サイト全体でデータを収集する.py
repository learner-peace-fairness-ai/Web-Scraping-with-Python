import requests
from bs4 import BeautifulSoup
import re

pages = set()


def get_links(page_url):
    global pages

    url = f'https://en.wikipedia.org{page_url}'

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    try:
        print(soup.h1.get_text())
        print(soup.find(id='mw-content-text').find_all('p')[0])
        print(soup.find_all(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! No worries though!')

    for link in soup.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' not in link.attrs:
            continue

        if link['href'] not in pages:
            # 新しいページに出会った
            new_page = link['href']
            print(new_page)
            print(f'----------------\n{new_page}')
            pages.add(new_page)

            get_links(new_page)


get_links('')
