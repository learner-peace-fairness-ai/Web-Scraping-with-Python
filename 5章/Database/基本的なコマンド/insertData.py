from datetime import datetime
import sqlite3

sqlite3.register_adapter(datetime, lambda dt: int(dt.timestamp()))
sqlite3.register_converter("TIMESTAMP", lambda dt: datetime.fromtimestamp(int(dt)))

with sqlite3.connect('scraping', detect_types=sqlite3.PARSE_DECLTYPES) as con:
    con.execute('INSERT INTO pages (title, content) VALUES ("Test page title", "This is some test page content. It can be up to 10,000 characters long.")')
    
    dt = (datetime.fromisoformat("2014-09-21 10:25:32"),)
    con.execute('INSERT INTO pages (id, title, content, created) VALUES (3, "Test page title", "This is some test page content. It can be up to 10,000 characters long.", ?)', dt)
