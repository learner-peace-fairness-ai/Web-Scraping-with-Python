import unittest
from unittest import TestCase

from bs4 import BeautifulSoup
import requests


class TestWikipedia(TestCase):
    soup = None

    @classmethod
    def setUpClass(cls):
        URL = "https://en.wikipedia.org/wiki/Monty_Python"

        res = requests.get(URL)
        cls.soup = BeautifulSoup(res.text, "html.parser")

    def test_titleText(self):
        soup = TestWikipedia.soup

        page_title = soup.find("h1").get_text()
        self.assertEqual("Monty Python", page_title)

    def test_contentExists(self):
        soup = TestWikipedia.soup

        content = soup.find("div", {"id": "mw-content-text"})
        self.assertIsNotNone(content)


if __name__ == "__main__":
    unittest.main()
