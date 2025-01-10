from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import ssl
import certifi
from bs4 import BeautifulSoup


def get_site_html(url):
    context = ssl.create_default_context(cafile=certifi.where())

    try:
        response = urlopen(url, context=context)
    except HTTPError as e:
        print(e)
        return None
    except URLError:
        print('The server could not be found!')
        return None

    return response.read()


def get_title(html):
    try:
        bsObj = BeautifulSoup(html, 'html.parser')
        title = bsObj.body.h1
    except AttributeError:
        return None

    return title


url = 'https://pythonscraping.com/pages/page1.html'
html = get_site_html(url)

if html:
    title = get_title(html)

    if title == None:
        print('Title could not be found')
    else:
        print(title)
