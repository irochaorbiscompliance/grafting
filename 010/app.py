import csv
import sqlite3
dbh = sqlite3.connect('010.sqlite')
cursor = dbh.cursor()

with open("/Users/islrocha/Desktop/FILE/DEV/grafting/010/export.csv") as csv_file:
    csvfile = csv.reader(csv_file, delimiter = ',')
    all_value = []
    for row in csvfile:
        value = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        all_value.append(value)
        
query = "INSERT INTO 'products'('make', 'model', 'description', 'psu_ext_v', 'psu_ext_a', 'psu_ext_w') VALUES (%s, %s, %s, %s, %s, %s, %s)"
cursor = dbh.cursor()
cursor.executemany(query, all_value)
dbh.commit()