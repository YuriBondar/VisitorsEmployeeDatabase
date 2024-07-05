
from inputFieldsFunctions import *

def fCreateNewEmployee():

    employeesPositions = (
        "Status: Mitarbeiter*inn oder Besucher*inn",
        "Nachname",
        "Vorname",
        "Position"
        "Telefonnummer",
        "E-Mail",
        "Sozialversicherungsnummer",
        "Arbeitet im Unternehmen seit:")

    employee = ["Employee"]

    employee.append(fInputAndCheckName("Nachname"))
    employee.append(fInputAndCheckName("Vorname"))
    employee.append(fInputAndCheckTitle())
    employee.append(fInputAndCheckTel())
    employee.append(fInputAndCheckEmail())
    employee.append(fInputAndCheckInsuranceNumber())
    employee.append(fInputAndCheckStartDate())
    return employee


    # for i in    r ange(2):
    #     while True:
    #         userInput = input(f"Input {employeesPositions[i]} :")
    #         if isString(userInput):
    #             employee[i] = userInput
    #             break
    #         else:
    #             print("Incorrect Input. Input nur letters")

    # while True:
    #     userInput = input(f"Input Telefonnummer (11 Zahlen):")
    #     if isPhone(userInput):
    #         employee[4] = userInput
    #         break

    employee[4]









def fCreateNewVisitor():
    pass

def isEmployeeInDatabase():
    pass

def fAddVisitor():
    pass

def fcorrectVisitor():
    pass