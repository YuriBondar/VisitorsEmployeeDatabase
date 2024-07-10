
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
    #     Status: Mitarbeiter*inn
    #     Nachname
    #     Vorname
    #     Geschlecht"
    #     Title",
    #     Sozialversicherungsnummer"
    #     E-Mail",
    #     Telefonnummer",
    #     Adresse: Ort, Straße, Hausnummer
    #     Geburtsdatum

    employee = ["Mitarbeiter*inn"]

    while True:
        userInput = input("Nachname: ")
        if (fCheckWord(userInput, False)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Vorname: ")
        if (fCheckWord(userInput, False)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Geschlecht(m oder w): ")
        if (fCheckGeschlecht(userInput)):
            employee.append(userInput)
            if userInput == "m":
                employee[0] = "Mitarbeiter"
            else:
                employee[0] = "Mitarbeiterin"
            break

    while True:
        userInput = input("Title:")
        if (fCheckWord(userInput, True)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Sozialversicherungsnummer: ")
        if (fCheckInsurance(userInput)):
            employee.append(userInput)
            break

    while True:
        userInput = input("E-mail: ")
        if (fCheckEmail(userInput)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Telefonnummer: ")
        if (fChekPhone(userInput)):
            patternForRemove = r'^[ -\)\(]$'
            userInput = re.sub(patternForRemove, '', userInput)
            employee.append(userInput)
            break

    while True:
        userInput = input("Adresse. Ort: ")
        if (fCheckWord(userInput, True)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Adresse. Straße: ")
        if (fCheckWord(userInput, True)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Adresse. Hausnummer: ")
        if (fCheckHaus(userInput)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Geburtsdatum (format: dd.mm.yyyy):")
        if (fCheckDate(userInput)):
            employee.append(userInput)
            break

    return employee
def fCreateNewVisitor():
    #     Daten für den Mitarbeiter:
    #     Status: Besucher*inn
    #     Nachname
    #     Vorname
    #     E-Mail
    #     Telefonnummer
    #     Verantwortlicher Manager
    #     Tag und Zeit des Besuchs

    visitor = ["Visitor*inn"]

    while True:
        userInput = input("Nachname: ")
        if (fCheckWord(userInput, False)):
            visitor.append(userInput)
            break

    while True:
        userInput = input("Vorname: ")
        if (fCheckWord(userInput, False)):
            visitor.append(userInput)
            break

    while True:
        userInput = input("E-mail: ")
        if (fCheckEmail(userInput)):
            visitor.append(userInput)
            break

    while True:
        userInput = input("Telefonnummer: ")
        if (fChekPhone(userInput)):
            visitor.append(userInput)
            break

    while True:
        userInput = input("Verantwortlicher Manager: ")
        if (fCheckWord(userInput, False)):
            visitor.append(userInput)
            break

    while True:
        userInput = input("Tag und Zeit des Besuchs: ")
        if (fCheckDate(userInput)):
            visitor.append(userInput)
            break
    return visitor

def selectRecord(userChoise, userChoiseString, typeOfPerson):
    if typeOfPerson == "Employee":
        fullDictinary = fileToDictionary("Employees.csv")
    else:
        fullDictinary = fileToDictionary("Visitors.csv")
    selectDictinary = {}
    print(f"Geben Sie {userChoiseString} ein, nach dem Sie suchen möchten:")
    neededAttribute = input()
    for personNumber, personData in fullDictinary.items():
        if neededAttribute == personData[userChoise-1]:
            selectDictinary[personNumber] = personData
    return selectDictinary

def identifyOnlyRecord(selectresults, typeOfPerson):
    if typeOfPerson == "Employee":
        typeOfPerson = "Mitarbeiter"
    else:
        typeOfPerson = "Besucher"
    print(f"Ihre Suche ergab folgende {typeOfPerson}")
    print(selectresults)
    print(f"Wählen Sie die Nummer des {typeOfPerson} aus, um die Daten zu ändern")
    neededPersonNumber = input(f"{typeOfPerson} ")
    neededPerson = typeOfPerson + neededPersonNumber
    return selectresults[neededPerson]

def changeCurrentPerson(selectresults, typeOfPerson):
    pass