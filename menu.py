
from changeFunctions import *
from mainmenuGUI import mainmenuGUI
from selectFunctions import *

#----------------------------------------------------------------------
#--------------------  main menu-----------------------------------------
#----------------------------------------------------------------------
def mainMenu():

    while True:

        mainmenuGUI()

        print(f"-------------------------------------------------------")
        print(f"-------------------------------------------------------")
        print("Willkommen in der Datenbank!")
        print(f"-------------------------------------------------------")
        print("Wählen die Option:")
        printList(getMainMenuItems())
        userChoice = input("Ihre Auswahl:")
        if not checkUserChoiseInMenu(userChoice, len(getMainMenuItems())-1):
            continue
        else:
            userChoice = int(userChoice)
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
                case 9:
                    printBirthdaysEmployee()
                case 10:
                    break
                case _:
                    print("Geben Sie eine Zahl aus den Menüpunkten")

