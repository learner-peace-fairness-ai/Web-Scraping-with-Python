import requests

URL = 'https://pythonscraping.com/pages/page1.html'

response = requests.get(URL)
print(response.text)
