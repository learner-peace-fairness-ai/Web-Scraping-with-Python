import requests

res = requests.get('https://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
print(res.text)
