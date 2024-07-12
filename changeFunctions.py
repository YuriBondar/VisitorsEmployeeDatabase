from addFunctions import *
from dataFunctions import *
from selectFunctions import *


def ChooseOnePerson(selectresults, typeOfPerson):
    typeOfPersonGer = translateTypeOfPerson(typeOfPerson)
    if len(selectresults) > 1:
        print(f"Ihre Suche ergab folgende {typeOfPersonGer}")
        printDictinary(selectresults, typeOfPerson)
        print(f"Wählen Sie die Nummer des {typeOfPersonGer} aus, um die Daten zu ändern")
        neededPersonNumber = input(f"{typeOfPersonGer} ")
        neededPerson = typeOfPersonGer + " " + neededPersonNumber
        return {neededPerson: selectresults[neededPerson]}
    else:
        return selectresults

def changeCurrentPerson(currentPerson, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    if typeOfPerson == "Employee":
        fullDictinary = fileToDictionary("Employee")
    else:
        fullDictinary = fileToDictionary("Visitor")

    while True:
        print(f"Wählen Sie aus, nach welchem Attribut Sie {typeOfPerson}informationen ändern möchten:")
        printList(atributesList)
        attributeToChange = input("Ihre Auswahl:")
        newData = None
        while True:
            newData = input(f"Inpute new {atributesList[int(attributeToChange)-1]}:")
            if checkData(attributeToChange, newData, typeOfPerson):
                break
        key = list(currentPerson.keys())[0]
        currentPerson[key][int(attributeToChange)-1] = newData

        fullDictinary[key] = currentPerson.get(key)
        writeToFile(fullDictinary,typeOfPerson)
        print(f"Do you want to change another attribute for this person? (y/n)")
        userchoice = input("Ihre Auswahl: ")
        if userchoice == "n":
            break

def changeRecordsInterface(typeOfPerson):

    while True:
        print(f"-------------------------------------------------------")
        print(f"-------------------------------------------------------")
        print(f" Menu Korrekturen")
        print(f"-------------------------------------------------------")
        print(f" 1.Suchen Sie den {typeOfPerson}, dessen Daten Sie korrigieren möchten")
        print(f" 2.Geben Sie den Nachnamen des {typeOfPerson}s ein")
        print(f" 3.Zurück zum Hauptmenü")
        userChoise = input("Ihre Auswahl:")
        if not checkUserChoiseInMenu(userChoise, 3):
            continue
        elif int(userChoise) == 3:
            return
        elif int(userChoise) == 1:
            selectresults = selectRecordsInterface(typeOfPerson, True)
        elif int(userChoise) == 2:
            neededAtribute = input("Nachname: ")
            selectresults = selectByAttribute(1, neededAtribute, typeOfPerson)

        currentPerson = ChooseOnePerson(selectresults, typeOfPerson)
        changeCurrentPerson(currentPerson, typeOfPerson)
