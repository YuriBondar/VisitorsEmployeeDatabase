
from changeFunctions import *
from selectFunctions import *

#----------------------------------------------------------------------
#--------------------main menu-----------------------------------------
#----------------------------------------------------------------------
def mainMenu():

    menuItems = ["Neuen Eintrag für Mitarbeiter*innen erstellen",
                 "Neuen Eintrag für Besucher*innen erstellen",
                 "Mitarbeiterinformationen suchen/anzeigen",
                 "Vollständige Mitarbeiterdatenbank anzeigen",
                 "Besucherinformationen suchen/anzeigen",
                 "Vollständige Besucherdatenbank anzeigen",
                 "Mitarbeiterinformationen ändern",
                 "Besucherinformationen ändern",
                 "Aus der Datenbank auswählen"]

    while True:
        print(f"-------------------------------------------------------")
        print(f"-------------------------------------------------------")
        print(f"-------------------------------------------------------")
        print("Willkommen in der Datenbank!")
        print(f"-------------------------------------------------------")
        print("Wählen die Option:")
        printList(menuItems)
        userChoice = int(input("Ihre Auswahl:"))

        match userChoice:
            case 1:
                addNewRecordInterface("Employee")
            case 2:
                addNewRecordInterface("Visitor")
            case 3:
                selectRecordsInterface("Employee", False)
            case 4:
                printFullDatabase("Employee")
            case 5:
                selectRecordsInterface("Visitor", False)
            case 6:
                printFullDatabase("Visitor")
            case 7:
                changeRecordsInterface("Employee")
            case 8:
                changeRecordsInterface("Visitor")
            case 7:
                break
            case _:
                print("Geben Sie eine Zahl aus den Menüpunkten")

