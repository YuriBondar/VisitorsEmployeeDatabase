
import datetime

#----------------------------------------------------------------------
#Modul für Datenprüfungsfunktionen
#-----------------------------------------------------------------------
def isEmpty(userInput):
    if userInput == "":
        print("Dieses Feld darf nicht leer sein")
        return True
    else:
        return False
def fCheckWord(userInput, isPoint):
    if isPoint == True:
        mylist = "abcdefghijklmnopqrstuvwxyzöäüß -."
    else:
        mylist = "abcdefghijklmnopqrstuvwxyzöäüß -"

    if isEmpty(userInput):
        return False
    elif userInput[0] == "-" or userInput[0] == "." or userInput[len(userInput)-1] == "-":
        print("An erster oder letzter Stelle muss ein Buchstabe stehen.")
        return False
    elif all(letter.lower() in mylist for letter in userInput):
        return True
    else:
        if isPoint == True:
            print("Geben Sie nur Buchstaben, Leerzeichen, Punkt oder das Zeichen '-' ein.")
            return False
        else:
            print("Geben Sie nur Buchstaben, Leerzeichen oder das Zeichen '-' ein")
            return False

def fCheckGeschlecht(userInput):
    if userInput == "m" or userInput == "w":
        return True
    else:
        print("Geben Sie nur 'm' oder 'w' ein.")
        return False

def fCheckEmail(userInput):
    mylist = "abcdefghijklmnopqrstuvwxyz0123456789.-_@"
    if isEmpty(userInput):
        return False
    elif userInput[0] == "@" or userInput[0] == "@":
        print("Die E-Mail-Adresse darf nicht mit '@' beginnen oder enden.")
        return False
    elif userInput.count("@") != 1:
        print("Die E-Mail-Adresse muss genau einen @-Symbol enthalten.")
        return False
    else:
        splitEmail = userInput.rsplit("@")
        if all('.' not in letter for letter in splitEmail[1]):
            print("Die E-Mail-Adresse muss mindestens einen Punkt nach dem @-Symbol enthalten.")
            return False
        elif (splitEmail[0][0] == "." or
              splitEmail[0][len(splitEmail[0])-1] == "." or
              splitEmail[1][0] == "." or
              splitEmail[1][len(splitEmail[1])-1] == "." or
              splitEmail[1][0] == "-" or
              splitEmail[1][len(splitEmail[1])-1] == "-"):
            print("Incorrect Email")
            return False
        elif all(letter.lower() in mylist for letter in userInput):
            return True
        else:
            print("Geben Sie nur Buchstaben, Leerzeichen, Punkt oder das Zeichen '-' ein.")
            return False

def fChekPhone(userInput):
    mylist = "0123456789()- "
    if isEmpty(userInput):
        return False
    elif all(letter.lower() in mylist for letter in userInput):
        return True
    else:
        print("Bitte geben Sie nur Zahlen, Leerzeichen oder folgende Symbole: '-', '(',')' ein.")
        return False
def fCheckInsurance(userInput):
    if isEmpty(userInput):
        return False
    elif len(userInput) != 8:
        print("Die Sozialversicherungsnummer muss aus 8 Zahlen bestehen")
        return False
    elif userInput.isnumeric():
        return True
    else:
        return False

def fCheckHaus(userInput):
    mylist = "abcdefghijklmnopqrstuvwxyz0123456789-/"
    if isEmpty(userInput):
        return False
    elif not userInput[0].isnumeric():
        print("An erster Stelle muss ein Zahl stehen.")
        return False
    else:
        if all(letter.lower() in mylist for letter in userInput):
            return True
        else:
            print("Geben Sie nur Buchstaben, Zahlen, oder folgende Symbole: '-', '/' ein.")
            return False


def fInputAndCheckStartDate(userInput):
    if isEmpty(userInput):
        return False
    elif userInput[2] != "." and userInput[5] != ".":
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
