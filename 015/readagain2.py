import sqlite3
con = sqlite3.connect("/Users/islrocha/Desktop/FILE/DEV/grafting/015/database.db")
con.row_factory = sqlite3.Row
cur = con.cursor()
cur.execute('SELECT * FROM products')

r = cur.fetchone()
print(r.keys())
print(r['id'])
print(r['make'])
print(r['model'])