import sqlite3

with sqlite3.connect('scraping') as con:
    cur = con.execute('SELECT * FROM pages WHERE id = 2')
    print(cur.fetchall())

    cur = con.execute('SELECT id, title FROM pages WHERE content LIKE "%page content%"')
    print(cur.fetchall())
