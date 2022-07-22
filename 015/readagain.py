import sqlite3
import sys
print(sys.version)

try:
    dbh = sqlite3.connect('/Users/islrocha/Desktop/FILE/DEV/grafting/014/database.db')
    dbh.row_factory = sqlite3.Row
    cursor = dbh.cursor()
    
    sql = "SELECT * FROM products"
    
    cursor.execute(sql)
    
    rows = cursor.fetchall()
    #print(rows)
    for x in rows:
        print(x)
    
    cursor.close()
    
except sqlite3.Error as e:
    print("Error while Retrieving Results", e)
    
finally:
    if (dbh):
        dbh.close()
        print("Connection Closed")