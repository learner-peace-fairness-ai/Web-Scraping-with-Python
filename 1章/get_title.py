import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        response = requests.get(url)
    except HTTPError as e:
        print(e)
        return None

    html = response.text

    try:
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.body.h1
    except AttributeError as e:
        print(e)
        return None

    return title


title = get_title('https://pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)
