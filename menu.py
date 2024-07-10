import csv
import os
from databaseFunctions import *
from dataFunctions import *

#--------------------------------------------------------
def menuAddNewRecord(typeOfPerson):
    if typeOfPerson == "Employee":
        fileName = "Employees.csv"
    else:
        fileName = "Visitors.csv"
    if not os.path.exists(fileName):
        print(f"Achtung, die Datenbank mit {typeOfPerson} wurde nicht gefunden. Es wird eine neue Mitarbeiterdatenbank erstellt.")
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        if fileName == "Employees.csv":
            writer.writerow(fCreateNewEmployee())
        else:
            writer.writerow(fCreateNewVisitor())
#--------------------------------------------------------

#----------------------------------------------------------------------
#----------------select menu-------------------------------------------
#----------------------------------------------------------------------
def menuSelect(typeOfPerson, isCorrection):

    atributesList = chooseAtributesList(typeOfPerson)

    while True:
        print("Wählen Sie aus, nach welchem Attribut Sie Mitarbeiterinformationen auswählen möchten:")
        printList(atributesList)
        print(f"{len(atributesList) + 1}. Zurück zum Hauptmenü")

        userChoise = input("Ihre Auswahl:")
        if not checkUserChoiseInMenu(userChoise, len(atributesList) + 1):
            continue
        elif userChoise == (len(atributesList) + 1):
            break
        else:
            resultSelection = selectRecord(userChoise, atributesList[userChoise-1], typeOfPerson)
            if isCorrection == True:
                return resultSelection
            elif resultSelection == {}:
                print(f"Keine Ergebniss für {atributesList[userChoise-1]} {neededAttribute}")
            else:
                print(f"Suchergebnisse: \n{resultSelection}")
    input("Eine beliebige Taste drücken")


def menuChange(typeOfPerson):

    print(f" 1.Suchen Sie den {typeOfPerson}, dessen Daten Sie korrigieren möchten")
    print(f" 2.Geben Sie den Nachnamen des {typeOfPerson}s ein")
    userChoise = input()
    if userChoise == 1:
        selectresults = menuSelect(typeOfPerson, True)
    elif userChoise == 2:
        selectresults = selectRecord(2, userChoise, typeOfPerson)

    if len(selectresults) > 1:
        selectresults = identifyOnlyRecord(selectresults, typeOfPerson)

    changeCurrentPerson(selectresults, typeOfPerson)



#----------------------------------------------------------------------
#--------------------main menu-----------------------------------------
#----------------------------------------------------------------------
def mainMenu():

    menuItems = ["Neuen Eintrag für Mitarbeiter*innen erstellen",
                 "Neuen Eintrag für Besucher*innen erstellen",
                 "Mitarbeiterinformationen suchen/anzeigen",
                 "Vollständige Mitarbeiterdatenbank anzeigen"
                 "Besucherinformationen suchen/anzeigen",
                 "Vollständige Besucherdatenbank anzeigen"
                 "Mitarbeiterinformationen ändern",
                 "Besucherinformationen ändern",
                 "Aus der Datenbank auswählen"]

    print("Willkommen in der Datenbank!")
    while True:
        print("Wählen die Option:")
        printList(menuItems)
        status = int(input("Ihre Auswahl:"))

        match status:
            case 1:
                menuAddNewRecord("Employee")
            case 2:
                menuAddNewRecord("Visitor")
            case 3:
                menuSelect("Employee", False)
            case 4:
                menuSelect("Visitor", False)
            case 5:
                printDatabase("Employee")
            case 6:
                printDatabase("Visitor")
            case 7:
                menuChange("Employee")
            case 8:
                menuChange("Visitor")
            case 7:
                break
            case _:
                print("Geben Sie eine Zahl aus den Menüpunkten")