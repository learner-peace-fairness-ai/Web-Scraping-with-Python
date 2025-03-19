from csv import DictReader
from io import StringIO

import requests

res = requests.get('https://pythonscraping.com/files/MontyPythonAlbums.csv')
data = res.content.decode(encoding='ascii', errors='ignore')
with StringIO(data) as buffer:
    dict_reader = DictReader(buffer)

    print(dict_reader.fieldnames)

    for row in dict_reader:
        print(row)
