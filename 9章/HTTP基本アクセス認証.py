import requests
from requests.auth import HTTPBasicAuth

URL = "https://pythonscraping.com/pages/auth/login.php"

auth = HTTPBasicAuth("ryan", "password")
res = requests.post(URL, auth=auth)

print(res.text)
