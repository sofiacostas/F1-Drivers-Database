# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'cars_relationships.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect('F1_drivers.db')
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()


menu_choice = ''
while menu_choice != 'Z':
    menu_choice = input("Welcome to F1 drivers(As of July 2025 and not including sprints) Database!\n\n"
                        "Type the letter for the information you want: \n"
                        "A: Drivers from United Kingdom\n"
                        "B: Youngest to oldest\n"
                        "C: Drivers older than 25 years old\n")
    
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query("United Kingdom drivers stats")
    elif menu_choice == 'B': 
        print_query("All drivers youngest to oldest")
    elif menu_choice == 'C': 
        print_query("Older than 25")
