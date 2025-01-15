import requests
from requests.exceptions import HTTPError
from requests.exceptions import ConnectionError

URL = 'https://pythonscrapingthisurldoesnotexist.com'

try:
    response = requests.get(URL)
except HTTPError as e:
    print(e)
except ConnectionError:
    print('The server could not be found!')
else:
    print('It Worked!')
