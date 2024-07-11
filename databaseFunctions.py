
from checkFunctions import *
from dataFunctions import *
import csv


#----------------------------------------------------------------------
#Modul für Datenbankfunktionen:
# 1.Hinzufügen eines Mitarbeiters
# 2.Hinzufügen eines Besuchers
#-----------------------------------------------------------------------
def fCreateNewEmployee():

    # Daten für den Mitarbeiter
    #     Nachname
    #     Vorname
    #     Geschlecht"
    #     Title",
    #     Sozialversicherungsnummer"
    #     E-Mail",
    #     Telefonnummer",
    #     Adresse: Ort, Straße, Hausnummer
    #     Geburtsdatum

    employee = []

    while True:
        userInput = input("Nachname: ")
        if (checkWord(userInput, False)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Vorname: ")
        if (checkWord(userInput, False)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Geschlecht(m oder w): ")
        if (checkGeschlecht(userInput)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Title:")
        if (checkWord(userInput, True)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Sozialversicherungsnummer: ")
        if (checkInsurance(userInput)):
            employee.append(userInput)
            break

    while True:
        userInput = input("E-mail: ")
        if (checkEmail(userInput)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Telefonnummer: ")
        if (chekPhone(userInput)):
            patternForRemove = r'^[ -\)\(]$'
            userInput = re.sub(patternForRemove, '', userInput)
            employee.append(userInput)
            break

    while True:
        userInput = input("Adresse. Ort: ")
        if (checkWord(userInput, False)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Adresse. Straße: ")
        if (checkWord(userInput, True)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Adresse. Hausnummer: ")
        if (checkHaus(userInput)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Geburtsdatum (format: dd.mm.yyyy):")
        if (checkDate(userInput)):
            employee.append(userInput)
            break

    return employee
def fCreateNewVisitor():
    #     Daten für den Mitarbeiter:
    #     Nachname
    #     Vorname
    #     E-Mail
    #     Telefonnummer
    #     Verantwortlicher Manager
    #     Tag und Zeit des Besuchs

    visitor = []

    while True:
        userInput = input("Nachname: ")
        if (checkWord(userInput, False)):
            visitor.append(userInput)
            break

    while True:
        userInput = input("Vorname: ")
        if (checkWord(userInput, False)):
            visitor.append(userInput)
            break

    while True:
        userInput = input("E-mail: ")
        if (checkEmail(userInput)):
            visitor.append(userInput)
            break

    while True:
        userInput = input("Telefonnummer: ")
        if (chekPhone(userInput)):
            visitor.append(userInput)
            break

    while True:
        userInput = input("Verantwortlicher Manager: ")
        if (checkWord(userInput, False)):
            visitor.append(userInput)
            break

    while True:
        userInput = input("Tag und Zeit des Besuchs: ")
        if (checkDate(userInput)):
            visitor.append(userInput)
            break
    return visitor

def selectByAttribute(userChoise, neededAttribute, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    if typeOfPerson == "Employee":
        fullDictinary = fileToDictionary("Employees.csv")
    else:
        fullDictinary = fileToDictionary("Visitors.csv")
    selectDictinary = {}
    for personNumber, personData in fullDictinary.items():
        if neededAttribute == personData[userChoise-1]:
            selectDictinary[personNumber] = personData
    return selectDictinary

def identifyCurrentPerson(selectresults, typeOfPerson):
    if typeOfPerson == "Employee":
        typeOfPerson = "Mitarbeiter"
    else:
        typeOfPerson = "Besucher"
    if len(selectresults) > 1:
        print(f"Ihre Suche ergab folgende {typeOfPerson}")
        print(selectresults)
        print(f"Wählen Sie die Nummer des {typeOfPerson} aus, um die Daten zu ändern")
        neededPersonNumber = input(f"{typeOfPerson} ")
        neededPerson = typeOfPerson + neededPersonNumber
        return selectresults[neededPerson]
    else:
        return selectresults

def changeCurrentPerson(currentPerson, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    if typeOfPerson == "Employee":
        fullDictinary = fileToDictionary("Employees.csv")
    else:
        fullDictinary = fileToDictionary("Visitors.csv")

    while True:
        print(f"Wählen Sie aus, nach welchem Attribut Sie {typeOfPerson}informationen ändern möchten:")
        printList(atributesList)
        attributeToChange = input("Ihre Auswahl:")
        newData = None
        while True:
            newData = input(f"Inpute new {atributesList[attributeToChange-1]}:")
            if checkData(attributeToChange, newData, typeOfPerson):
                break
        key = list(currentPerson.keys())[0]
        currentPerson[key][attributeToChange-1] = newData

        fullDictinary[key] = currentPerson.get(key)
        writeToFile(fullDictinary,typeOfPerson)
        print(f"Do you want to change another attribute for this person? (y/n)")
        userchoice = input("Ihre Auswahl: ")
        if userchoice == "n":
            break


