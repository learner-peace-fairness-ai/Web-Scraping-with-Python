from collections import defaultdict
from random import randint

import requests


def sum_word_count_dict(word_count_dict):
    sum = 0
    for count in word_count_dict.values():
        sum += count
    return sum


def retrieve_random_word(word_count_dict):
    rand_index = randint(1, sum_word_count_dict(word_count_dict))

    for word, count in word_count_dict.items():
        rand_index -= count
        if rand_index <= 0:
            return word


def buid_word_dict(text):
    # 改行と引用符を除く
    text = text.replace('\n', ' ')
    text = text.replace('"', '')

    # 句読点が「語」として扱い、マルコフ連鎖に含める
    punctuation = [',',  '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, f' {symbol} ')

    words = text.split()

    word_dict = {}
    for i in range(1, len(words)):
        first_word  = words[i - 1]
        second_word = words[i]
        if first_word not in word_dict:
            # この語から新たな辞書を作る
            word_dict[first_word] = defaultdict(int)
        word_dict[first_word][second_word] += 1
    return word_dict


res = requests.get('https://pythonscraping.com/files/inaugurationSpeech.txt')
text = res.text
two_word_dict = buid_word_dict(text)

# 長さ100のマルコフ連鎖を生成する
length = 100
chain = ''
current_word = 'I'
for i in range(0, length):
    chain += f'{current_word} '
    second_word_count_dict = two_word_dict[current_word]
    current_word = retrieve_random_word(second_word_count_dict)

print(chain)
