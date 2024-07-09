import csv
import os
from databaseFunctions import *

#-------------------------------------------------------
def printMenu(menuItems):
    i = 0
    for menuItem in menuItems:
        i = i + 1
        print(f"{i}. {menuItem}")
    return i
#--------------------------------------------------------
def fAddNewRecord(fileName):
    if not os.path.exists(fileName):
        print("Achtung, die Datenbank mit Ihren Mitarbeitern wurde nicht gefunden. Es wird eine neue Mitarbeiterdatenbank erstellt.")
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        if fileName == "Employees.csv":
            writer.writerow(fCreateNewEmployee())
        else:
            writer.writerow(fCreateNewVisitor())

def fPrintFile(fileName):
    try:
        with open(fileName, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except Exception as e:
        print("Die Datenbank mit Ihren Mitarbeitern wurde nicht gefunden")
#----------------------------------------------------------------------
#-----------------------------------------------------------
#----------------------------------------------------------------------
def showEmployee():
    employeeAtributesList = ["Status",
        "Nachname",
        "Vorname",
        "Geschlecht",
        "Title",
        "Sozialversicherungsnummer",
        "E-Mail",
        "Telefonnummer",
        "Ort",
        "Straße",
        "Hausnummer",
        "Geburtsdatum"]

    print("Daten Wählen nach:")
    lastNumber = printMenu(employeeAtributesList) + 1
    print(f"{lastNumber}. Die Liste der Mitarbeiter*innen anzeigen")
    userChoise = int(input())
    selectData(employeeAtributesList[userChoise])








#----------------------------------------------------------------------
#--------------------main menu-----------------------------------------
#----------------------------------------------------------------------
def fMainMenu():

    menuItems = ["Neuen Eintrag für Mitarbeiter*innen erstellen",
                 "Neuen Eintrag für Besucher*innen erstellen",
                 "Die Liste der Mitarbeiter*innen anzeigen",
                 "Die Liste der Besucher*innen anzeigen",
                 "Die Arbeit mit der Datenbank beenden",
                 "Aus der Datenbank auswählen"]

    print("Willkommen in der Datenbank!")
    while True:
        print("Wählen die Option:")
        printMenu(menuItems)
        status = int(input())

        match status:
            case 1:
                fAddNewRecord("Employees.csv")
            case 2:
                fAddNewRecord("Visitors.csv")
            case 3:
                showEmployee()
            case 4:
                fPrintFile('Visitors.csv')
            case 5:
                fPrintFile('Visitors.csv')
            case 6:
                break
            case _:
                print("Geben Sie eine Zahl aus den Menüpunkten")