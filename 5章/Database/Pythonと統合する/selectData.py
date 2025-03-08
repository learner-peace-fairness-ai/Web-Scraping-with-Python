from datetime import datetime
import sqlite3

sqlite3.register_adapter(datetime, lambda dt: dt.isoformat())
sqlite3.register_converter('DATETIME', lambda dt: datetime.fromisoformat(dt.decode()))

with sqlite3.connect('scraping', detect_types=sqlite3.PARSE_DECLTYPES) as con:
    cur = con.execute('SELECT * FROM pages WHERE id=1')
    print(cur.fetchone())
