
from inputFieldsFunctions import *

# def fCreateNewEmployee():
#
#     employeesPositions = (
#         "Status: Mitarbeiter*inn oder Besucher*inn",
#         "Nachname",
#         "Vorname",
#         "Title"
#         "E-Mail",
#         "Telefonnummer",
#         "Sozialversicherungsnummer",
#         "Arbeitet im Unternehmen seit:")
#
#
#     employee = ["Employee"]
#     employee.append(fInputAndCheckName("Nachname"))
#     employee.append(fInputAndCheckName("Vorname"))
#     employee.append(fInputAndCheckTitle())
#     employee.append(fInputAndCheckTel())
#     employee.append(fInputAndCheckEmail())
#     employee.append(fInputAndCheckInsuranceNumber())
#     employee.append(fInputAndCheckStartDate())
#     return employee

def fCheckData(personalData, userInput):

    if userInput == "":
        print(f"Geben Sie {personalData} ein")
        return False
    else:

        if personalData == "Nachname" or personalData == "Vorname" or personalData == "Verantwortlicher Manager":
            mylist = "abcdefghijklmnopqrstuvwxyz -"
            for letter in userInput:
                if letter.lower() in mylist:
                    continue
                else:
                    print("Geben Sie nur Buchstaben, Leerzeichen oder das Zeichen '-' ein")
                    return False
            return True

        if personalData == "Title":
            mylist = "abcdefghijklmnopqrstuvwxyz -."
            for letter in userInput:
                if letter.lower() in mylist:
                    continue
                else:
                    print("Geben Sie nur Buchstaben, Leerzeichen, Punkt oder das Zeichen '-' ein.")
                    return False
            return True

        if personalData == "E-Mail":
            mylist = "abcdefghijklmnopqrstuvwxyz .@"
            isMail = False
            for letter in userInput:
                if letter.lower() in mylist:
                    if letter == "@":
                        isMail = True
                    continue
                else:
                    print("Geben Sie nur Buchstaben, Leerzeichen, Punkt oder das Zeichen '@' ein.")
                    return False
            if isMail == False:
                print("Die E-Mail-Adresse muss das Zeichen '@' enthalten.")
                return False
            else:
                return True

        if personalData == "Telefonnummer":
            mylist = "0123456789 ()+"
            for letter in userInput:
                if letter.lower() in mylist:
                    continue
                else:
                    print("Geben Sie nur Zahlen und folgende Zeichen: ),(,+ ein")
                    return False
            return True

        if personalData == "Sozialversicherungsnummer":
            if len(userInput) != 8:
                print("Die Sozialversicherungsnummer muss aus 8 Zahlen bestehen")
                return False
            else:
                for letter in userInput:
                    if letter.lower().isnumeric():
                        continue
                    else:
                        print("Geben Sie nur Zahlen ein")
                        return False
            return True


def fCreateNewEmployeeV2():
    employeeData = (
        "Status: Mitarbeiter*inn",
        "Nachname",
        "Vorname",
        "Title",
        "E-Mail"
        "Telefonnummer",
        "Sozialversicherungsnummer",
        "Arbeitet im Unternehmen seit:")

    employee = ["Mitarbeiter*inn"]

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


    # for i in range(2):
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











def fCreateNewVisitor():
    pass

def isEmployeeInDatabase():
    pass

def fAddVisitor():
    pass

def fcorrectVisitor():
    pass