import sqlite3

with sqlite3.connect("wikipedia.db") as con:
    con.execute(
        '''CREATE TABLE pages(
        id INTEGER PRIMARY KEY,
        url VARCHAR(255) NOT NULL,
        created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        )'''
    )

    con.execute(
        '''CREATE TABLE links(
        id INTEGER PRIMARY KEY,
        fromPageId INTEGER,
        toPageId INTEGER,
        created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        )'''
    )
