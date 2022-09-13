# Bookly Inventory project

### Introduction

Bookly is a local bookstore who needs to better understand and track their
inventory. To do this, all of their stock was entered by hand into an Excel
spreadsheet. With 1000 unique books in their catalog, it is becoming difficult
to sort through the large amount of data they have collected via Excel.

Bookly has decided to hire you to add all of this data into their newly
configured database server. They have already setup the server and exported the
Excel document into a more easily machine readable CSV file (book_inventory.csv).

### Task 1
#### Tools needed:
- python
- the book_inventory.csv file

#### Objective:
You will need to write a python program to do the following:
  1. Make sure you can read the contents of the CSV file
    1. Import the csv library
    2. Open the csv file
    3. Read the contents
    4. Skip the first line of the CSV file. This is just column titles (aka
       headers) which are not going to be important to us.
    5. Print each line, one by one

This will demonstrate the ability to import libraries, read files, and
manipulate the data contained within those files.

#### Hints
- Open the file by using "with open(FILENAME)"
- Loop over each line using a "for" statement

### Task 2
#### Tools needed:
- the mysql-connector-python library (install this with your code editor)

#### MySQL connection information:
  host="192.168.1.91" # This is the IP address of the database server
  user="nurhan"
  password="example-password"
  database="bookly"

#### Table information:
The table name is 'inventory'

Available fields:
  title
  category
  star_rating
  price
  stock
  quantity

You must provide data for all fields when inserting new records. No field can be
left empty.

There is an additional field called 'book_id'. You cannot add information to
this field directly. It's data type is 'integer' and it automatically adds a
number when a record is added to the table. For example, if there are no records
in the table and you add one, the 'book_id' for that record will be 0001. If you
add another record, that new record will have a 'book_id' of 0002.

#### Objective:
After opening, reading, and printing each line, you should be able to see that
each line in this csv file would equate to one record in the database. It is
your job to prepare that data to be sent to the database.

Note 1: Notice that, when printing the lines from the CSV file, each line is a
list of values.

Note 2: The mysql library only accepts tuples (a datatype similar to lists) as
input for the values of a database record.

1. Add configuration for the mysql connector. Refer to the data provided in the
   'MySQL connection information' section of this task.
2. Create a new function called sqlinsert().
  1. This function should accept one argument called "line"
  2. Convert the "line" input variable to a tuple.
  3. Write the mysql 'INSERT INTO' query for the table using the provided table
     format.
  4. Create a cursor using the mysql.connector library
  5. Use the cursor to execute the insert statement and the converted value.
  6. Commit to the database. This is what actually sends the data to the server.

3. Update your code from the previous task to send each line of the CSV file to
   the newly created sqlinsert() function.

4. Run your script to see if you successfully inserted the data.

#### Helpful tools:
I have created a script which will delete all records from the database if you
want to start with a clean, empty table. It is called 'clean_inventory.py'. You
can run it.

There is one more script where you can view the contents of the database. It is
called 'query_database.py'. The configuration is good for a sample of the data
included but of course you can modify it as you need.

### Task 3

#### Background:

Bookly has noticed that some of the books in it's database are incorrectly
labeled. Specifically, the Category for some books are labeled as "Default" or
"Add a comment" instead of a proper category. 

#### Objective:

Your task is to modify all of the affected records in MySQL to use a common
Category name. In this case, "Uncategorized" was decided to be the most
appropriate substitute.

Note 1: Do not reuse the python script you wrote to insert the records. Write a
new script that will be used specifically for updating these records that
already exist in the database.

Note 2: You can use the same method for logging into the mysql server as you did
in the previous task.

1. Find all of the affected records in the 'inventory' table.
    1. Use a SELECT sql query with a WHERE clause to make this easy
2. print() all of those records
3. Your program should now ask you to confirm if the rows that were printed in
   the previous step are the correct records. It should wait for you to type
   'yes' before going any further in your program.
4. If you enter anything other than 'yes' your program should exit (aka quit).
5. If you enter 'yes' your program should update all of the records printed in
   step 2 of this task to "Uncategorized".
    1. Use an UPDATE sql query. Remember to only to change the database records
       where (<- hint) the category is incorrectly entered. If you are updating
       records which are unaffected by this mislabelling, you would essentially
       be ruining legitimate data in a real world situation.
6. Your program should print a message saying the update is completed.
7. Re-running the same program should run the same SELECT sql query. If your
   previous UPDATE was successfully executed, there should be zero records
   returned. You will have completed Task 3.

#### Let me know if you need any help. :)
