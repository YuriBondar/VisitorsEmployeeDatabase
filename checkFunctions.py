
import datetime
import re

#----------------------------------------------------------------------
#Modul für Datenprüfungsfunktionen
#-----------------------------------------------------------------------

def fCheckWord(userInput, isPoint):
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

def fCheckGeschlecht(userInput):
    if userInput == "m" or userInput == "w":
        return True
    else:
        print("Geben Sie nur 'm' oder 'w' ein.")
        return False

def fCheckEmail(userInput):
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

def fChekPhone(userInput):
    patternForRemove = r'^[ -\)\(]$'
    pattern = r'^[0-9 -]+$'
    userInput = re.sub( patternForRemove, '', userInput)

    if re.match(pattern, userInput) is None or len(userInput) != 11:
        print("Ungültige Telefonnummer")
        return False
    else:
        return True

def fCheckInsurance(userInput):
    if len(userInput) != 8:
        print("Die Sozialversicherungsnummer muss aus 8 Zahlen bestehen")
        return False
    elif userInput.isnumeric():
        return True
    else:
        return False

def fCheckHaus(userInput):
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


def fCheckDate(userInput):
    if userInput[2] != "." and userInput[5] != ".":
        print("Incorrect Date. Format: dd.mm.yyyy")
        return False
    else:
        dataList = userInput.rsplit(".")
        try:
            startDay = datetime.datetime(int(dataList[2]), int(dataList[1]), int(dataList[0]))
            if startDay <= datetime.datetime.now():
                return True
        except ValueError:
            print(f"Incorrect Date. Format: dd.mm.yyyy")
            return False
