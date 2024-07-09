import csv
import os
from databaseFunctions import *

#-------------------------------------------------------
def fPrintMenu(menuItems):
    i = 0
    for menuItem in menuItems:
        i = i + 1
        print(f"{i}. {menuItem}")
#--------------------------------------------------------
def fAddNewRecord(fileName):
    if not os.path.exists(fileName):
        print("Achtung, die Datenbank mit Ihren Mitarbeitern wurde nicht gefunden. Es wird eine neue Mitarbeiterdatenbank erstellt.")
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        if fileName == "Employees.cvs":
            writer.writerow(fCreateNewEmployee())
        else:
            writer.writerow(fCreateNewVisitor())

def fPrintFile(fileName):
    try:
        if os.path.exists(fileName):
            with open(fileName, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
    except Exception as e:
        print("")
def fMenu():

    menuItems = ["Neuen Eintrag für Mitarbeiter*innen erstellen",
                 "Neuen Eintrag für Besucher*innen erstellen",
                 "Die Liste der Mitarbeiter*innen anzeigen",
                 "Die Liste der Besucher*innen anzeigen",
                 "Die Arbeit mit der Datenbank beenden"]

    print("Willkommen in der Datenbank!")
    while True:
        print("Wählen die Option:")
        fPrintMenu(menuItems)
        status = input()

        if status == "1":
            fAddNewRecord("Employees.cvs")
        if status == "2":
            fAddNewRecord("Visitors.cvs")
        if status == "3":
            with open('Employees.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        if status == "4":
            with open('Visitors.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        if status == "5":
            break