
from datetime import datetime
import re

#----------------------------------------------------------------------
#Modul für Datenprüfungsfunktionen
#-----------------------------------------------------------------------

def checkWord(userInput, isPoint):
    if isPoint == True:
        pattern = r'^([a-zA-ZüäößÜÄÖß][a-zA-ZüäößÜÄÖß \-\.]*[a-zA-ZüäößÜÄÖß \.])?$'
    else:
        pattern = r'^[a-zA-ZüäößÜÄÖß][a-zA-ZüäößÜÄÖß \-]*([a-zA-ZüäößÜÄÖß ])?$'

    if re.match(pattern, userInput) is not None:
        return True
    else:
        if isPoint == True:
            print("Geben Sie nur Buchstaben, Leerzeichen, Punkt oder das Zeichen '-' ein.\n"
                  "Das Feld darf nicht leer sein.\n"
                  " An der ersten und letzten Position darf kein Bindestrich stehen.")
            return False
        else:
            print("Geben Sie nur Buchstaben, Leerzeichen, oder das Zeichen '-' ein.\n"
                  "An der ersten Position darf kein Bindestrich und Punkt stehen\n"
                  "An der letzten Position darf kein Bindestrich stehen ")
            return False

def checkGeschlecht(userInput):
    if userInput == "m" or userInput == "w":
        return True
    else:
        print("Geben Sie nur 'm' oder 'w' ein.")
        return False

def checkEmail(userInput):
    pattern = r'^[\wÜÄÖß\+\.-]+@[\wÜÄÖß\+-]+\.[\wÜÄÖß\+-\.]+$'
    errorMassage = "Ungültige Email"

    if re.match(pattern, userInput) is None:
        print(errorMassage)
        return False
    else:
        localPart, domainPart = userInput.split('@')
        domains = domainPart.split('.')
        if localPart[0] == "." or localPart[len(localPart)-1] == ".":
            print(errorMassage)
            return False
        elif ".." in localPart:
            print(errorMassage)
            return False
        else:
            for domain in domains:
                if domain == "" or domain[0] == "-" or localPart[len(localPart)-1] == "-":
                    print(errorMassage)
                    return False
    return True

def chekPhone(userInput):
    patternForRemove = r'[ -\)\(]'
    pattern = r'^[0-9]{11}+$'
    userInput = re.sub(patternForRemove, '', userInput)

    if re.match(pattern, userInput) is False:
        print("Ungültige Telefonnummer")
        return False
    else:
        return userInput

def checkInsurance(userInput):
    if len(userInput) != 10:
        print("Die Sozialversicherungsnummer muss aus 10 Zahlen bestehen")
        return False
    elif userInput.isnumeric():
        return True
    else:
        return False

def checkSrteetHouse(userInput):
    pattern = r'^[a-zA-ZüäößÜÄÖß][a-zA-ZüäößÜÄÖß \-\.]+[0-9]+([a-zA-ZüäößÜÄÖß \-\.\\])?$'
    pass
def checkHaus(userInput):
    mylist = "abcdefghijklmnopqrstuvwxyz0123456789-/"
    if not userInput[0].isnumeric():
        print("An erster Stelle muss ein Zahl stehen.")
        return False
    else:
        if all(letter.lower() in mylist for letter in userInput):
            return True
        else:
            print("Geben Sie nur Buchstaben, Zahlen, oder folgende Symbole: '-', '/' ein.")
            return False


def checkDate(userInput):
    try:
        startDay = datetime.strptime(userInput, "%d.%m.%Y")
        if startDay <= datetime.now():
            return True
        else:
            print("das Datum ist noch nicht gekommen")
            return False
    except ValueError:
        print(f"Incorrect Date. Format: dd.mm.yyyy")
        return False

def checkData (userChoice, newData, typeOfPerson):

    if typeOfPerson == "Employee":
        match int(userChoice):
            case 1 | 2 | 8:
                return checkWord(newData,False)
            case 3 | 9:
                return checkGeschlecht(newData)
            case 4:
                return checkWord(newData,True)
            case 5:
                return checkInsurance(newData)
            case 6:
                return checkEmail(newData)
            case 7:
                return chekPhone(newData)
            case 10:
                return checkHaus(newData)
            case 11:
                return checkDate(newData)
            case _:
                return False
    elif typeOfPerson == "Visitor":
        match int(userChoice):
            case 1 | 2 | 5:
                return checkWord(newData,False)
            case 3:
                return checkEmail(newData)
            case 4:
                return chekPhone(newData)
            case 6:
                return checkDate(newData)
            case _:
                return False


def checkUserChoiseInMenu(userChoise, lastNumber):
    if not userChoise.isnumeric():
        print("Geben Sie eine Nummer aus der Liste ein")
        return False
    else:
        userChoise = int(userChoise)
        if userChoise < 1 or userChoise > lastNumber:
            print("Geben Sie eine Nummer aus der Liste ein")
            input("Eine beliebige Taste drücken")
            return False
        else:
            return True
