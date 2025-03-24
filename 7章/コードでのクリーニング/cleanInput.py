import re
import string

from bs4 import BeautifulSoup
import requests


def clean_input(input):
    input = re.sub('\n+', ' ', input)
    input = re.sub('\[[0-9]*\]', '', input)
    input = re.sub(' +', ' ', input)
    input = bytes(input, 'utf-8')
    input = input.decode('ascii', 'ignore')

    clean_input = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            clean_input.append(item)
    return clean_input


def get_ngrams(input, n):
    input = clean_input(input)
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i + n])
    return output


res = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
html = res.text
soup = BeautifulSoup(html, 'html.parser')
content = soup.select_one('#mw-content-text').get_text()

ngrams = get_ngrams(content, 2)
print(ngrams)
print(f'2-grams count is: {len(ngrams)}')
