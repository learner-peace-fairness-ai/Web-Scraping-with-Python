import re
import sqlite3
import time

from bs4 import BeautifulSoup
import requests

DB_NAME = 'wikipedia.db'
WAIT_SEC = 1
pages = set()


def insert_page_if_not_exists(url):
    with sqlite3.connect(DB_NAME) as con:
        cur = con.execute('SELECT * FROM pages WHERE url = ?', (url,))
        rows = cur.fetchall()
        if len(rows) == 0:
            cur.execute('INSERT INTO pages (url) VALUES (?)', (url,))
            return cur.lastrowid
        else:
            url_id = rows[0][0]
            return url_id


def insert_link(from_page_id, to_page_id):
    with sqlite3.connect(DB_NAME) as con:
        cur = con.execute('SELECT * FROM links WHERE fromPageId = ? AND toPageId = ?', (from_page_id, to_page_id))
        rows = cur.fetchall()
        if len(rows) == 0:
            cur.execute('INSERT INTO links (fromPageId, toPageId) VALUES (?, ?)', (from_page_id, to_page_id))


def get_links(page_url, recursion_level):
    global pages

    if recursion_level > 4:
        return

    page_id = insert_page_if_not_exists(page_url)
    res = requests.get(f'https://en.wikipedia.org{page_url}')
    res.raise_for_status()
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    for link in soup.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
        link_url = link['href']

        insert_link(page_id, insert_page_if_not_exists(link_url))
        if link_url not in pages:
            # 新しいページに出会う、追加してリンクを探す
            new_page = link_url
            pages.add(new_page)

            time.sleep(WAIT_SEC)
            get_links(new_page, recursion_level + 1)


get_links('/wiki/Kevin_Bacon', 0)
