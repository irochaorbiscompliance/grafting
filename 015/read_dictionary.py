import sqlite3

conn = sqlite3.connect("/Users/islrocha/Desktop/FILE/DEV/grafting/015/database.db")

#This is the important part, here we are setting row_factory property of
#connection object to sqlite3.Row(sqlite3.Row is an implementation of
#row_factory)
conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute('SELECT * FROM products')

result = c.fetchall()
#returns a list of dictionaries, each item in list(each dictionary)
#represents a row of the table

from pprint import pprint
pprint(vars(result))