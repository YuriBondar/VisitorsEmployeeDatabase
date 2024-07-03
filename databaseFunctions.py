
from inputFieldsFunctions import *


def fCreateNewEmployeeV2():
    employeeData = (
        "Status: Mitarbeiter*inn",
        "Nachname",
        "Vorname",
        "Title",
        "E-Mail",
        "Telefonnummer",
        "Sozialversicherungsnummer",
        "Arbeitet im Unternehmen seit:")

    employee = ["Mitarbeiter*inn"]

    while True:
        userInput = input(f"Input Nachname :")
        if isEmpty(userInput):
            if (fCheckName(userInput)):
                employee.append(userInput)
                break

    while True:
        userInput = input(f"Input Vorname :")
        if isEmpty(userInput):
            if (fCheckName(userInput)):
                employee.append(userInput)
                break


    for i in range(5):
        while True:
            userInput = input(f"Input {employeeData[i+1]} :")
            if fCheckData(employeeData[i+1], userInput):
                employee.append(userInput)
                break

    employee.append(fInputAndCheckStartDate())
    return employee

def fCreateNewVisitor():
    visitorData = (
        "Status: Visitor*inn",
        "Nachname",
        "Vorname",
        "E-Mail"
        "Telefonnummer",
        "Verantwortlicher Manager",
        "Tag und Zeit des Besuchs")

    visitor = ["Visitor*inn"]

    for i in range(4):
        while True:
            userInput = input(f"Input {visitorData[i + 1]} :")
            if fCheckData(visitorData[i + 1], userInput):
                visitor.append(userInput)
                break

    visitor.append(fInputAndCheckStartDate())
    return visitor













def fCreateNewVisitor():
    pass

def isEmployeeInDatabase():
    pass

def fAddVisitor():
    pass

def fcorrectVisitor():
    pass