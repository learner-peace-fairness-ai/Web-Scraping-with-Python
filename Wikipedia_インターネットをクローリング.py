from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse
import ssl
import certifi
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now().timestamp())


# ページで見つかったすべての内部リンクのリストを取り出す
def get_internal_links(soup, include_url):
    internal_links = []
    # "/"で始まるすべてのリンクを見つける
    for link in soup.find_all('a', href=re.compile(r'^(\/|.*' + include_url + ')')):
        url = link['href']

        if url is None:
            continue

        if url.startswith('/'):
            url = include_url + url

        if url not in internal_links:
            internal_links.append(url)

    return internal_links


# ページで見つかったすべての外部リンクのリストを取り出す
def get_external_links(soup, exclude_url):
    external_links = []
    # 現在のURLを含まない"http"か"www"で始まるすべてのリンクを見つける
    for link in soup.find_all('a', href=re.compile(r'^(http|www)((?!' + exclude_url + ').)*$')):
        url = link['href']

        if url is None:
            continue

        if url not in external_links:
            external_links.append(url)

    return external_links


def get_random_external_link(starting_page):
    context = ssl.create_default_context(cafile=certifi.where())
    html = urlopen(starting_page, context=context)
    soup = BeautifulSoup(html, 'html.parser')

    scheme = urlparse(starting_page).scheme
    network_location = urlparse(starting_page).netloc

    external_links = get_external_links(soup, network_location)
    if len(external_links) == 0:
        print('No external links, looking around the site for one')
        domain = f'{scheme}://{network_location}'

        internal_links = get_internal_links(soup, domain)
        internal_link = internal_links[random.randint(
            0, len(internal_links) - 1)]
        return get_random_external_link(internal_link)
    else:
        return external_links[random.randint(0, len(external_links) - 1)]


def follow_external_only(starting_site):
    external_link = get_random_external_link(starting_site)
    print(f'Random external link is {external_link}')
    follow_external_only(external_link)


follow_external_only('https://oreilly.com')
