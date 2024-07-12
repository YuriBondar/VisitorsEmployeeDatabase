import csv
import os
from addFunctions import *
from dataFunctions import *

def selectByAttribute(userChoise, neededAttribute, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    if typeOfPerson == "Employee":
        fullDictinary = fileToDictionary("Employee")
    else:
        fullDictinary = fileToDictionary("Visitor")
    selectDictinary = {}
    for personNumber, personData in fullDictinary.items():
        if neededAttribute in personData[int(userChoise)-1]:
            selectDictinary[personNumber] = personData
    return selectDictinary
def selectRecordsInterface(typeOfPerson, isCorrection):

    atributesList = chooseAtributesList(typeOfPerson)
    typeOfPersonGer = translateTypeOfPerson(typeOfPerson)

    while True:
        print(f"-------------------------------------------------------")
        print(f"-------------------------------------------------------")
        print(f"Filtermunü")
        print(f"-------------------------------------------------------")
        print(f"Wählen Sie aus, nach welchem Attribut Sie {typeOfPersonGer}informationen auswählen möchten:")
        printList(atributesList)
        print(f"{len(atributesList) + 1}. Zurück zum Hauptmenü")

        userChoise = input("Ihre Auswahl:")

        if not checkUserChoiseInMenu(userChoise, len(atributesList) + 1):
            continue
        elif int(userChoise) == (len(atributesList) + 1):
            return
        else:
            print(f"Geben Sie {atributesList[int(userChoise) - 1]} ein, nach dem Sie suchen möchten:")
            neededAttribute = input()
            resultSelection = selectByAttribute(userChoise, neededAttribute, typeOfPerson)
            if isCorrection == True:
                return resultSelection
            elif resultSelection == {}:
                print(f"Keine Ergebniss für {atributesList[int(userChoise)-1]} {neededAttribute}")
            else:
                print(f"Suchergebnisse:")
                printDictinary(resultSelection,typeOfPerson)
        userChoise = input(f"Möchten Sie weitere Informationen auswählen über {typeOfPerson} (y/n)")
        if userChoise == "n":
            return