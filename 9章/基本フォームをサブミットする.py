import requests

URL = "https://pythonscraping.com/pages/files/processing.php"
PARAMS = {"firstname": "Ryan", "lastname": "Mitchell"}

res = requests.post(URL, data=PARAMS)
print(res.text)
