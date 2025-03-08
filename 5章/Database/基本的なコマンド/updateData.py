import sqlite3

with sqlite3.connect('scraping') as con:
    con.execute('UPDATE pages SET title="A new title", content="Some new content" WHERE id=3')
