from urllib.request import urlopen
from urllib.error import HTTPError
import ssl
import certifi
from bs4 import BeautifulSoup


def get_title(url):
    context = ssl.create_default_context(cafile=certifi.where())

    try:
        html = urlopen(url, context=context)
    except HTTPError as e:
        print(e)
        return None

    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.body.h1
    except AttributeError:
        return None

    return title


title = get_title('https://pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)
