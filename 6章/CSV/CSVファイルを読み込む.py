import csv
from io import StringIO

import requests

res = requests.get('https://pythonscraping.com/files/MontyPythonAlbums.csv')
data = res.content.decode(encoding='ascii', errors='ignore')
with StringIO(data) as buffer:
    csv_reader = csv.reader(buffer)

    for row in csv_reader:
        print(row)
