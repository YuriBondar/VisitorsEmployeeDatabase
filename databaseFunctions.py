
from inputFieldsFunctions import *


def fCreateNewEmployeeV2():

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
        if isEmpty(userInput):
            if (fCheckName(userInput)):
                employee.append(userInput)
                break

    while True:
        userInput = input("Vorname: ")
        if isEmpty(userInput):
            if (fCheckName(userInput)):
                employee.append(userInput)
                break

    while True:
        userInput = input("Geschlecht(m oder w): ")
        if isEmpty(userInput):
            if (fCheckGeschlecht(userInput)):
                employee.append(userInput)
                if userInput == "m":
                    employee[0] = "Mitarbeiter"
                else:
                    employee[0] = "Mitarbeiterinn"

                break

    while True:
        userInput = input("Title:")
        if (fCheckTitle(userInput)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Sozialversicherungsnummer: ")
        if isEmpty(userInput):
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
            employee.append(userInput)
            break

    while True:
        userInput = input("Adresse. Ort: ")
        if (fCheckName(userInput)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Adresse. Straße: ")
        if (fCheckName(userInput)):
            employee.append(userInput)
            break

    while True:
        userInput = input("Geburtsdatum: ")
        if (fInputAndCheckStartDate()):
            employee.append(userInput)
            break


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
        if isEmpty(userInput):
            if (fCheckName(userInput)):
                visitor.append(userInput)
                break

    while True:
        userInput = input("Vorname: ")
        if isEmpty(userInput):
            if (fCheckName(userInput)):
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
        if isEmpty(userInput):
            if (fCheckName(userInput)):
                visitor.append(userInput)
                break

    while True:
        userInput = input("Tag und Zeit des Besuchs: ")
        if (fInputAndCheckStartDate()):
            visitor.append(userInput)
            break

