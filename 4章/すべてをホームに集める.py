import random
import re
import time

import requests
from bs4 import BeautifulSoup

WAIT_SECONDS = 1


def get_links(articul_url):
    response = requests.get(f'https://en.wikipedia.org{articul_url}')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    link_list = soup.select('div#bodyContent a[href^="/wiki/"]')
    return [link for link in link_list if re.search('((?!:).)*', link['href'])]


def get_history_ip_addresses(page_url):
    # 変更履歴ページのフォーマットは：
    # https://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    page_url = page_url.replace('/wiki/', '')
    history_url = f'https://en.wikipedia.org/w/index.php?title={page_url}&action=history'
    print(f'history_url is: {history_url}')
    response = requests.get(history_url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # ユーザ名の代わりにIPアドレスを持つ"mw-anonuserlink"クラスのリンクだけを見つける
    ip_addresses = soup.select('a.mw-anonuserlink')
    address_list = set()
    for ip_address in ip_addresses:
        address_list.add(ip_address.get_text())
    return address_list


links = get_links('/wiki/Python_(programming_language)')

while len(links) > 0:
    for link in links:
        print('-------------------')
        history_ip_addresses = get_history_ip_addresses(link['href'])
        for history_ip in history_ip_addresses:
            print(history_ip)

    new_link = links[random.randint(0, len(links)-1)].attrs['href']
    print(f'new_link is: {new_link}')
    links = get_links(new_link)
    
    time.sleep(WAIT_SECONDS)
