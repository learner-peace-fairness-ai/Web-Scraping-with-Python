from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import ssl
import certifi


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


url = 'https://pythonscraping.com/pages/page1.html'
html = get_site_html(url)
print(html)
