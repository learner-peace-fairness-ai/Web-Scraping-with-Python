from collections import defaultdict
import re
from operator import itemgetter
import re
import string

import requests


def is_common(word):
    common_words = [
        'a', 'about', 'all', 'also', 'an', 'and', 'as', 'at',
        'be', 'because', 'been', 'but', 'by',
        'can','come', 'could',
        'day','do',
        'find', 'first', 'for', 'from',
        'get','give', 'go', 
        'has', 'have', 'he', 'her', 'here', 'him', 'his', 'how',
        'i', 'if', 'in', 'into', 'is', 'it', 'its',
        'just', 
        'know',
        'like', 'look',
        'make', 'man', 'many', 'me', 'more', 'my',
        'new', 'no', 'not', 'now',
        'of', 'on', 'one', 'or', 'other', 'our', 'out',
        'people',
        'say', 'see', 'she', 'so', 'some',
        'take', 'than', 'that', 'the', 'them', 'then','there', 'these', 'they', 'their', 'thing', 'think', 'this', 'time', 'to', 'two',
        'up',
        'we', 'what', 'who', 'with', 'will', 'would',
        'use',
        'want', 'way', 'well', 'when', 'which',
        'year', 'you',  'your',
    ]

    for common_word in common_words:
        if re.search(fr'\b{common_word}\b', word):
            return True
    return False


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
sorted_ngrams = dict(sorted(ngrams.items(), key=itemgetter(1), reverse=True))

not_common_ngrams = {}
for word in sorted_ngrams:
    if is_common(word):
        continue
    
    not_common_ngrams[word] = sorted_ngrams[word]

not_common_and_more_than_3count_ngrams = {k: v for k, v in not_common_ngrams.items() if v >= 3}
print(not_common_and_more_than_3count_ngrams)
