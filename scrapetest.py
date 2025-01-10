import requests

html = requests.get(r'https://pythonscraping.com/pages/page1.html')
print(html.text)
