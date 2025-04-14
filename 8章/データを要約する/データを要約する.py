from collections import defaultdict
import re
from operator import itemgetter
import string

import requests


def clean_input(input):
    input = re.sub('\n+', ' ', input).lower()
    input = re.sub('\[[0-9]*\]', '', input)
    input = re.sub(' +', ' ', input)
    input = bytes(input, 'utf-8')
    input = input.decode('ascii', 'ignore')

    clean_input = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item == 'a' or item == 'i'):
            clean_input.append(item)
    return clean_input


def get_ngrams(input, n):
    input = clean_input(input)
    output = defaultdict(int)
    for i in range(len(input) - n + 1):
        ngram_temp = ' '.join(input[i:i + n])
        output[ngram_temp] += 1
    return output


res = requests.get('https://pythonscraping.com/files/inaugurationSpeech.txt')
content = res.text
ngrams = get_ngrams(content, 2)
sorted_ngrams = sorted(ngrams.items(), key=itemgetter(1), reverse=True)
print(sorted_ngrams)
