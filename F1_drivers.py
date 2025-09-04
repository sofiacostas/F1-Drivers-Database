# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'F1_drivers.db'

# This is the SQL to connect to all the tables in the database
TABLES = (" drivers_stats "
           "LEFT JOIN teams ON drivers_stats.team_id = teams.team_id "
           "LEFT JOIN nations ON drivers_stats.nation_id = nations.nation_id ")


def print_parameter_query(fields:str, where:str, parameter):
    """ Prints the results for a parameter query in tabular form. """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(tabulate(results,fields.split(",")))
    db.close()  

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
    menu_choice = input("Welcome to F1 drivers from 2025 Grid Database!\n\n"
    
    "PLEASE NOTE!: The following Database INCLUDES the following\n"
    "- Drivers who are on the grid as of July 2025\n"
    "- Their stats as of July 2025\n"
    "- The drivers career points AND podiums NOT their current season points AND podiums\n"
    "- The amount of races is the amount of starts\n"
    "- Sprints are not counted in the points or races\n\n"
    
                        "Type the letter for the information you want: \n"
                        "A: What team drivers are from\n"
                        "B: What nation drivers are from\n"
                        "C: Youngest to oldest\n"
                        "D: Older than 25 years old\n"
                        "E: Have 3 or more podiums\n"
                        "F: Drivers that have more than 75 races and more than 1000 career points\n"
                        "G: Aged 25 or older\n"
                        "H: Have no podiums\n"
                        "I: Drivers with at least 1 podium and 400 points\n"
                        "J: Less than 100 races\n"
                        "K: 100 or more races\n"
                        "L: Less than 500 points\n"
                        "M: In their 20s and have at least 30 races\n"
                        "N: Between 10 to 100 podiums\n"
                        "O: 35+ years old\n"     

                        "\nZ: Exit\n\n""Type option here: "                  
                        )
    
    menu_choice = menu_choice.upper()
    if menu_choice == 'A': 
        print('Here are the following teams to choose from\n'
              '- McLaren\n'
              '- Ferrari\n'
              '- Red Bull\n'
              '- Williams\n'
              '- Sauber\n'
              '- Racing Bulls\n'
              '- Aston Martin\n'
              '- Haas\n'
              '- Alpine\n')
        team = input('Which team do you want to see: ').capitalize()
        print_parameter_query("name, age, points", "team = ? ORDER BY points DESC",team)
    elif menu_choice == 'B': 
        print('Here are the following nations to choose from\n'
              '- Australia\n'
              '- United Kingdom\n'
              '- Monaco\n'
              '- Italy\n'
              '- Netherlands\n'
              '- Japan\n'
              '- Thailand\n'
              '- Spain\n'
              '- Germany\n'
              '- Brazil\n'
              '- New Zealand\n'
              '- France\n'
              '- Canada\n'
              '- Argentina\n')
        nation = input('Of what nation do you want to see players of: ').capitalize()
        print_parameter_query("name, age, points", "nation = ? ORDER BY points DESC",nation)
    elif menu_choice == 'C': 
        print_query("All drivers youngest to oldest")
    elif menu_choice == 'D': 
        print_query("Older than 25")
    elif menu_choice == 'E': 
        print_query("3 or more podiums")
    elif menu_choice == 'F': 
        print_query("More than 75 races and more than 1000 points")
    elif menu_choice == 'G': 
        print_query("Age 25 or younger")
    elif menu_choice == 'H': 
        print_query("No podiums")
    elif menu_choice == 'I': 
        print_query("At least 1 podium and 400 points")    
    elif menu_choice == 'J': 
        print_query("Less than 100 races")
    elif menu_choice == 'K': 
        print_query("100 or more races")
    elif menu_choice == 'L': 
        print_query("Less than 500 points")
    elif menu_choice == 'M': 
        print_query("In 20s and at least 30 races")
    elif menu_choice == 'N': 
        print_query("Between 10 to 100 podiums")
    elif menu_choice == 'O': 
        print_query("35+ years old")

