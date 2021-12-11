'''
This program demonstrates the Big Data concept
by implementing the SQL.

Author: Navjot Saini
Assignment: Hw 12 (Exercise 17.2)
'''

# import modules
import sqlite3
import pandas as pd
from tabulate import tabulate

# create connection object
connection = sqlite3.connect('books.db')

# set up
pd.options.display.max_columns = 10

# call connection cursos method
cursor = connection.cursor()

# use execute method to select data from table
cursor = cursor.execute('SELECT * FROM titles')

# fetch all the matching rows
print("Using the fetchall method:")
tuples = cursor.fetchall()
print(tuples)

# use description to see details
print("\n\nUsing the attribute description:")
print(cursor.description)

# diplay data in tabular format
print("\n\nDisplaying table in tabular format:")
print()
print(tabulate(tuples, headers=["ISBN", "Title", "Edition", "Copyright"]))


