from pathlib import Path
import requests

URL = "https://pythonscraping.com/pages/files/processing2.php"

with Path("helloworld.txt").open("rb") as fr:
    files = {"uploadFile": fr}

    res = requests.post(URL, files=files)

print(res.text)
