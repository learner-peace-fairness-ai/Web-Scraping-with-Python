import random
import re
import time
import unittest
from unittest import TestCase
from urllib.parse import unquote

from bs4 import BeautifulSoup
import requests


class TestWikipedia(TestCase):
    GENTLEMANLY_WAIT_SECONDS = 1
    soup = None

    def test_page_properties(self):
        wait_sec = TestWikipedia.GENTLEMANLY_WAIT_SECONDS
        url = "https://en.wikipedia.org/wiki/Monty_Python"

        # 最初の3ページをテストする
        for i in range(3):
            res = requests.get(url)
            TestWikipedia.soup = BeautifulSoup(res.text, "html.parser")

            page_title, url_title = self.title_matches_url(url)
            self.assertEqual(page_title, url_title)
            self.assertTrue(self.content_exists())

            url = self.get_next_link()
            time.sleep(wait_sec)
        print("Done!")

    def title_matches_url(self, url):
        soup = TestWikipedia.soup

        page_title = soup.find("h1").get_text()
        url_title = url[url.index("/wiki/") + 6 :]
        url_title = url_title.replace("_", " ")
        url_title = unquote(url_title)
        return (page_title, url_title)

    def content_exists(self):
        soup = TestWikipedia.soup

        content = soup.find("div", {"id": "mw-content-text"})
        return True if content else False

    def get_next_link(self):
        soup = TestWikipedia.soup

        body_content = soup.select_one("#bodyContent")
        links = body_content.find_all("a", href=re.compile("^(/wiki/)((?!:).)*$"))
        new_article = random.choice(links).attrs["href"]
        return f"https://en.wikipedia.org{new_article}"


if __name__ == "__main__":
    unittest.main()
