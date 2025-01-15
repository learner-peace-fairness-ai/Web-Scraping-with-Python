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

    for link in soup.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' not in link.attrs:
            continue

        if link['href'] not in pages:
            # 新しいページに出会った
            new_page = link['href']
            print(new_page)
            pages.add(new_page)

            get_links(new_page)


get_links('')
