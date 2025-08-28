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
    menu_choice = input("Welcome to F1 drivers from 2025 Grid Database!\n\n"
    
    "PLEASE NOTE!: The following Database INCLUDES the following\n"
    "- Drivers who are on the grid as of July 2025\n"
    "- Their stats as of July 2025\n"
    "- The drivers career points NOT their current season points\n"
    "- The drivers career podiums NOT their current season podiums\n"
    "- The amount of races is the amount of starts\n"
    "- Sprints are not counted in the points or races\n\n"
    
                        "Type the letter for the information you want: \n"
                        "A: From United Kingdom\n"
                        "B: Youngest to oldest\n"
                        "C: Older than 25 years old\n"
                        "D: Non European Drivers\n"
                        "E: Have 3 or more podiums\n"
                        "F: Drivers that have more than 75 races and more than 1000 career points\n"
                        "G: European Drivers\n"
                        "H: Aged 25 or older\n"
                        "I: Have no podiums\n"
                        "J: Drivers with at least 1 podium and 400 points\n"
                        "K: McLaren, Ferrari, Williams, Haas or Alpine drivers\n"
                        "L: Less than 100 races\n"
                        "M: 100 or more races\n"
                        "N: Asia and Oceania drivers\n"
                        "O: South and North America drivers\n"
                        "P: Mercedes, Red Bull, Sauber, Racing Bulls, or Aston Martin drivers\n"
                        "Q: Less than 500 points\n"
                        "R: In their 20s and have at least 30 races\n"
                        "S: Red Bull and Racing Bulls drivers\n"
                        "T: Between 10 to 100 podiums\n"
                        "U: 35+ years old\n"     

                        "\nZ: Exit\n\n""Type option here: "                  
                        )
    
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query("United Kingdom drivers stats")
    elif menu_choice == 'B': 
        print_query("All drivers youngest to oldest")
    elif menu_choice == 'C': 
        print_query("Older than 25")
    elif menu_choice == 'D': 
        print_query("Non European Drivers")
    elif menu_choice == 'E': 
        print_query("3 or more podiums")
    elif menu_choice == 'F': 
        print_query("More than 75 races and more than 1000 points")
    elif menu_choice == 'G': 
        print_query("European Drivers")
    elif menu_choice == 'H': 
        print_query("Age 25 or younger")
    elif menu_choice == 'I': 
        print_query("No podiums")
    elif menu_choice == 'K': 
        print_query("McLaren, Ferrari, Williams, Haas or Alpine drivers")
    elif menu_choice == 'L': 
        print_query("Less than 100 races")
    elif menu_choice == 'M': 
        print_query("100 or more races")
    elif menu_choice == 'N': 
        print_query("Asia and Oceania drivers")
    elif menu_choice == 'O': 
        print_query("North and South America drivers")
    elif menu_choice == 'P': 
        print_query("Mercedes, Red Bull, Sauber, Racing Bulls, or Aston Martin drivers")
    elif menu_choice == 'Q': 
        print_query("Less than 500 points")
    elif menu_choice == 'R': 
        print_query("In 20s and at least 30 races")
    elif menu_choice == 'S': 
        print_query("Red Bull and Racing Bulls")
    elif menu_choice == 'T': 
        print_query("Between 10 to 100 podiums")
    elif menu_choice == 'U': 
        print_query("35+ years old")

