# Import required modules
import csv
import sqlite3
 
# Connecting to the geeks database
connection = sqlite3.connect('013.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE products(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                make varchar(50),
                model varchar(50),
                description varchar(50),
                psu_ext_v double(3,3),
                psu_ext_a double(3,3),
                psu_ext_w double(3,3),
                psu_int_v integer(1),
                psu_int_w double(3,3),
                rj_45 int(1),
                a_v int(1),
                wireless int(1),
                hs_code int(8)
                );
                '''

# Creating the table into our database
cursor.execute(create_table)

# Opening the csv file
file = open('/Users/islrocha/Desktop/FILE/DEV/grafting/013/import.csv')

# Reading the contents of the csv file
contents = csv.reader(file)

# SQL query to insert data into the table
insert_records = "INSERT INTO products (make, model, description, psu_ext_v, psu_ext_a, psu_ext_w, psu_int_v, psu_int_w, rj_45, a_v, wireless, hs_code) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

# Importing the contents of the file into table
cursor.executemany(insert_records, contents)

# SQL query to retrieve all data from
# the table to verify that the
# data of the csv file has been successfully
# inserted into the table
select_all = "SELECT * FROM products"
rows = cursor.execute(select_all).fetchall()

# Output to the console screen
for r in rows:
    print(r)

# Committing the changes
connection.commit()
 
# closing the database connection
connection.close()