import sqlite3

with sqlite3.connect('scraping') as con:
    con.execute('CREATE TABLE pages(id integer primary key, title VARCHAR(200), content VARCHAR(10000), created timestamp DEFAULT CURRENT_TIMESTAMP)')
