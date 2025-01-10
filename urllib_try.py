from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import ssl
import certifi

context = ssl.create_default_context(cafile=certifi.where())

try:
    html = urlopen(
        'https://pythonscrapingthisurldoesnotexist.com', context=context)
except HTTPError as e:
    print(e)
except URLError:
    print('The server could not be found!')
else:
    print('It Worked!')
