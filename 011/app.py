import sqlite3
import csv
import sys
dbh = sqlite3.connect('/Users/islrocha/Desktop/FILE/DEV/grafting/011.sqlite')
cursor = dbh.cursor()
csv_data = csv.reader(open('/Users/islrocha/Desktop/FILE/DEV/grafting/011/export.csv'))
header = next(csv_data)

print("Importing the file")
for row in csv_data:
    print(row)
    cursor.execute("INSERT INTO products (make, model, description, psu_ext_v, psu_ext_a, psu_ext_w, hs_code) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')", row)
dbh.commit()
cursor.close()
print("Done")