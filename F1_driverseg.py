import easygui as eg
import sqlite3
from tabulate import tabulate

DB_NAME = 'F1_drivers.db'


TABLES = (" drivers_stats "
           "LEFT JOIN teams ON drivers_stats.team_id = teams.team_id "
           "LEFT JOIN nations ON drivers_stats.nation_id = nations.nation_id ")


def parameter_query(fields:str, where:str, parameter):
    """ Prints the results for a parameter query in tabular form. """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    eg.msgbox(tabulate(results,fields.split(",")))
    db.close()  

def query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    db = sqlite3.connect('F1_drivers.db')
    cursor = db.cursor()
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    eg.msgbox(tabulate(results,headings))
    db.close()


menu_choice = ''
while menu_choice != 'Z':
    menu_choice = eg.msgbox("Welcome to F1 drivers from 2025 Grid Database!\n\n", "Welcome Page!")
    
    eg.msgbox("PLEASE NOTE!: The following Database INCLUDES the following\n"
    "- Drivers who are on the grid as of July 2025\n"
    "- Their stats as of July 2025\n"
    "- The drivers career points AND podiums NOT their current season points AND podiums\n"
    "- The amount of races is the amount of starts\n"
    "- Sprints are not counted in the points or races\n\n", "Notes Page")
    
    msg = "What information do you want to know?"
    title = "Home Page"
    choices = ["What team drivers are from\n",
                        "What nation drivers are from\n",
                        "Youngest to oldest\n",
                        "Older than 25 years old\n",
                        "Have 3 or more podiums\n",
                        "Drivers that have more than 75 races and more than 1000 career points\n",
                        "Top 8 drivers with the most points\n",
                        "Have no podiums\n",
                        "Drivers with at least 1 podium and 400 points\n",
                        "Less than 100 races\n",
                        "100 or more races\n",
                        "Less than 500 points\n",
                        "In their 20s and have at least 30 races\n",
                        "Between 10 to 100 podiums\n",
                        "Top 5 drivers with the most podiums\n",
                        "EXIT"]
    
    choice = eg.choicebox(msg, title, choices)
    if choice == choices[2]:
        query("All drivers youngest to oldest")
    elif choice == choices[3]:
        query("Older than 25")
    elif choice == choices[4]:
        query("3 or more podiums")
    elif choice == choices[5]:
        query("More than 75 races and more than 1000 points")
    elif choice == choices[6]:
        query("Top 8 points")
    elif choice == choices[7]:
        query("No podiums")
    elif choice == choices[8]:
        query("At least 1 podium and 400 points")    
    elif choice == choices[9]:
        query("Less than 100 races")
    elif choice == choices[10]:
        query("100 or more races")
    elif choice == choices[1]:
        query("Less than 500 points")
    elif choice == choices[12]:
        query("In 20s and at least 30 races")
    elif choice == choices[13]:
        query("Between 10 to 100 podiums")
    elif choice == choices[14]:
        query("Top 5 podiums")

if choice == 'What team drivers are from': 
        eg.msgbox('Here are the following teams to choose from\n'
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
        parameter_query("name, age, points", "team = ? ORDER BY points DESC",team)
elif menu_choice == 'B': 
        eg.msgbox('Here are the following nations to choose from\n'
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
        parameter_query("name, age, points", "nation = ? ORDER BY points DESC",nation)