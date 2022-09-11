#!/usr/bin/env python3

import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.1.91",
    user="nurhan",
    password="example-password",
    database="bookly"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM inventory LIMIT 10"
mycursor.execute(sql)
records = mycursor.fetchall()

for record in records:
    record = list(record)
    print(record)
