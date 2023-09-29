

import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('Attens.db')
 
# cursor object
cursor_obj = connection_obj.cursor()


# Creating table
table1 = """ CREATE TABLE Table1 (
            Username VARCHAR(50) ,
            Password VARCHAR(50) 
        )"""

a="am"
b=123
cursor_obj.execute(table1)


cursor_obj.execute("""
INSERT INTO Table1 (Username, Password)
VALUES (?,?)
""", (a, b))


# conn.commit ()
print ( 'Data entered successfully.' ) 

 
