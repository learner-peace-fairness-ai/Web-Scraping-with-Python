from urllib.request import urlopen
import ssl
import certifi
from bs4 import BeautifulSoup
import re

pages = set()


def get_links(page_url):
    global pages

    context = ssl.create_default_context(cafile=certifi.where())
    html = urlopen(
        f'https://en.wikipedia.org{page_url}', context=context)
    soup = BeautifulSoup(html, 'html.parser')

    try:
        print(soup.h1.get_text())
        print(soup.find(id='mw-content-text').find_all('p')[0])
        print(soup.find_all(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! No worries though!')

    for link in soup.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            url = link['href']

            if url not in pages:
                # 新しいページに出会った
                new_page = url
                print(new_page)
                print(f'----------------\n{new_page}')
                pages.add(new_page)

                get_links(new_page)


get_links('')
