import sqlite3

DB_NAME = 'wikipedia.db'


def get_url(page_id):
    with sqlite3.connect(DB_NAME) as con:
        con.row_factory = sqlite3.Row
        cur = con.execute('SELECT url FROM pages WHERE id = ?', (int(page_id),))
        rows = cur.fetchall()
        if len(rows) == 0:
            return None
        
        first_row = rows[0]
        return first_row['url']


def get_link_ids(from_page_id):
    with sqlite3.connect(DB_NAME) as con:
        con.row_factory = sqlite3.Row
        cur = con.execute('SELECT toPageId FROM links WHERE fromPageId = ?', (int(from_page_id),))
        rows = cur.fetchall()
        if len(rows) == 0:
            return None
        
        link_ids = [r['toPageId'] for r in rows]
        return link_ids


def search_breadth(target_page_id, current_page_id, depth, nodes):
    if nodes is None or len(nodes) == 0:
        return None
    
    if depth < 0:
        return None

    if depth == 0:
        for node in nodes:
            if node == target_page_id:
                return [node]
        return None
    
    # 深さは0より大きい -- もっと深く!
    for node in nodes:
        found = search_breadth(target_page_id, node, depth -1, get_link_ids(node))
        if found:
            found_link_ids = found
            found_link_ids.append(node)
            return found_link_ids
    
    return None


START_NODE = 1

nodes = get_link_ids(START_NODE)
target_page_id = 3
for i in range(0, 5):
    print(f'depth{i}で実行')
    
    found = search_breadth(target_page_id, 1, i, nodes)
    if found:
        found_link_ids = found
        found_link_ids.append(START_NODE)
        found_link_ids.reverse()
        for node in found_link_ids:
            print(get_url(node))
        break

    print(f'depth{i}では見つからなかった')
