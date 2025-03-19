import requests

res = requests.get('https://www.pythonscraping.com/pages/warandpeace/chapter1.txt')
print(res.text)
