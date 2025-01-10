from urllib.request import urlopen
import ssl
import certifi

context = ssl.create_default_context(cafile=certifi.where())
html = urlopen('https://pythonscraping.com/pages/page1.html', context=context)
print(html.read())
