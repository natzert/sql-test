#!/usr/bin/env python3

import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.1.91",
    user="nurhan",
    password="example-password",
    database="bookly"
)

mycursor = mydb.cursor()
sql = "DELETE FROM inventory WHERE book_id > 0"
mycursor.execute(sql)
mydb.commit()

print("The database has been cleaned")
