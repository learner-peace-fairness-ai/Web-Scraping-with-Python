from bs4 import BeautifulSoup
from requests import Session

URL = ("https://www.whatismybrowser.com/"
       "developers/what-http-headers-is-my-browser-sending")
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)"
                  "AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
    "Accept": "text/html,application/xhtml+xml,application/xml;"
              "q=0.9,image/webp,*/*;q=0.8"
}

session = Session()
res = session.get(URL, headers=HEADERS)
soup = BeautifulSoup(res.text, "html.parser")
print(soup.find("table", {"class": "table-striped"}).get_text)
