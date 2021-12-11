'''
This program demonstrates the Big Data concept
by implementing the SQL.

Author: Navjot Saini
Assignment: Hw 12 (Exercise 17.1)
'''

# import modules
import sqlite3
import pandas as pd

# create connection object
connection = sqlite3.connect('books.db')
pd.options.display.max_columns = 10

# select all authors last names from authors table in descending order
print('LAST NAMES IN DESCENDING ORDER')
last_names = pd.read_sql('SELECT last FROM authors ORDER BY last DESC', connection)
print(last_names)

# select all book titles from titles table in ascending order
print('\n\nBOOK TITLES IN ASCENDING ORDER')
books = pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)
print(books)

# use INNER JOIN to select all books fo specific author
print('\n\nIMPLEMENTING INNER JOIN')
print(pd.read_sql("""SELECT title, copyright, titles.isbn
FROM author_ISBN
INNER JOIN titles
ON author_ISBN.isbn = titles.isbn
WHERE id = '3'
ORDER BY title""", connection).head())

# insert new author into authors table
print("\n\nINSERTING NEW AUTHOR 'KATHY SMID'")
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last)
VALUES ('Kathy', 'Smid')""")
print(pd.read_sql('SELECT * FROM authors', connection, index_col=['id']))

# insert new title for author in the author_ISBN table
print('\n\nINSERTING NEW TITLE ENTRIES INTO AUTHOR_ISBN TABLE')
cursor = cursor.execute("""INSERT INTO author_ISBN (id, isbn)
VALUES ('6', '0233304677')""")
print(pd.read_sql("""SELECT * FROM author_ISBN WHERE id='6'""", connection))

# insert new title for author in the titles table
print('\n\nINSERTING NEW TITLE ENTRIES INTO TITLES TABLE')
cursor = cursor.execute("""INSERT INTO titles (isbn, title, edition, copyright)
VALUES ('0233304677', 'Advanced Python', '1', '2021')""")
print(pd.read_sql("""SELECT * FROM titles WHERE isbn = '0233304677'""", connection))
