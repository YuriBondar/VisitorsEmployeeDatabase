
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

def addNewRecordInterface(typeOfPerson):
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


