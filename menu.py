import csv
import os
from databaseFunctions import *

#-------------------------------------------------------
def printList(listItems):
    i = 0
    for listItem in listItems:
        i = i + 1
        print(f"{i}. {listItem}")
    return i
#--------------------------------------------------------
def addNewRecord(fileName):
    if not os.path.exists(fileName):
        print("Achtung, die Datenbank mit Ihren Mitarbeitern wurde nicht gefunden. Es wird eine neue Mitarbeiterdatenbank erstellt.")
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        if fileName == "Employees.csv":
            writer.writerow(fCreateNewEmployee())
        else:
            writer.writerow(fCreateNewVisitor())

def printFile(fileName):
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
def selectMenu():
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

    while True:
        print("Wählen Sie aus, nach welchem Attribut Sie Mitarbeiterinformationen auswählen möchten:")
        printList(employeeAtributesList)
        lastNumber = len(employeeAtributesList) + 1
        print(f"{lastNumber}. Vollständige Mitarbeiterdatenbank anzeigen")
        lastNumber = lastNumber + 1
        print(f"{lastNumber}. Zurück zum Hauptmenü")
        userChoise = input()
        if not userChoise.isnumeric():
            print("Geben Sie eine Nummer aus der Liste ein")
            continue
        else:
            userChoise = int(userChoise)
            if userChoise < 1 or userChoise > lastNumber:
                print("Geben Sie eine Nummer aus der Liste ein")
                continue
            elif userChoise == lastNumber:
                break
            elif userChoise == lastNumber - 1:
                printFile("Employees.csv")
                break
            else:
                print("Suchergebnisse:")
                print(selectEmployee(userChoise, employeeAtributesList[userChoise-1]))
        print("Eine beliebige Taste drücken")



#----------------------------------------------------------------------
#--------------------main menu-----------------------------------------
#----------------------------------------------------------------------
def mainMenu():

    menuItems = ["Neuen Eintrag für Mitarbeiter*innen erstellen",
                 "Neuen Eintrag für Besucher*innen erstellen",
                 "Mitarbeiterinformationen suchen/anzeigen",
                 "Besucherinformationen finden/anzeigen",
                 "Die Arbeit mit der Datenbank beenden",
                 "Aus der Datenbank auswählen"]

    print("Willkommen in der Datenbank!")
    while True:
        print("Wählen die Option:")
        printList(menuItems)
        status = int(input())

        match status:
            case 1:
                addNewRecord("Employees.csv")
            case 2:
                addNewRecord("Visitors.csv")
            case 3:
                selectMenu()
            case 4:
                printFile('Visitors.csv')
            case 5:
                printFile('Visitors.csv')
            case 6:
                break
            case _:
                print("Geben Sie eine Zahl aus den Menüpunkten")