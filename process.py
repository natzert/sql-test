#!/usr/bin/env python3

# Needed to read the CSV file
import csv

# Needed to connect to the database
import mysql.connector

# Database connection information
mydb = mysql.connector.connect(
    host="192.168.1.91",  # This is the IP address of the database server
    user="nurhan",
    password="example-password",
    database="bookly"
)

# Accept an argument called 'line' which can only be a list
def sqlinsert(line: list):
    """ Used to insert records into mysql database """

    # mycursor is the thing that does the "typing" for you in the database.
    # Think of it like a robot you send to the database to do what you want.
    mycursor = mydb.cursor()

    # The sql insert statement. We use %s here as a place where our variables
    # (aka values) will be inserted.
    sql = "INSERT INTO inventory (title, category, star_rating, price, stock, quantity) VALUES (%s, %s, %s, %s, %s, %s)"

    # MySQL only accepts a tuple (different data type) as an input. However,
    # when we read from a CSV, we get a list. We need to convert from list to
    # tuple so that the mysql library can understand it.
    value = tuple(line)

    # Prepare to run the sql insert query using that converted data.
    mycursor.execute(sql, value)

    # This is what actually pushes the changes to the database. Without this,
    # no changes will be made.
    mydb.commit()

    # Informational message just to let you know something is happening.
    print("Record inserted.")

# Open the CSV file
with open('./books_scraped.csv', mode = 'r') as file:
    # Read the CSV file
    csv_file = csv.reader(file)

    # The CSV file has column titles (aka headers) on the first line. We don't
    # need these in the database becaut the database already has it's own
    # column titles. This part of the code skips the first line in the CSV file
    # when reading it.
    next(csv_file, None)

    # Read each line in the CSV file and send it to the sqlinsert() function.
    for line in csv_file:
        sqlinsert(line)
