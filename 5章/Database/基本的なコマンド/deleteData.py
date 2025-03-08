import sqlite3

with sqlite3.connect('scraping') as con:
    con.execute('DELETE FROM pages WHERE id = 1')
