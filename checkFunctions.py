
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
def fCheckName(userInput):
    mylist = "abcdefghijklmnopqrstuvwxyzöäüß -"
    # if userInput[0] == " " or userInput[0] == "-":
    #     print("An erster Stelle muss ein Buchstabe stehen.")
    #     return False
    # else:
    if all(letter.lower() in mylist for letter in userInput):
        return True
    else:
        print("Geben Sie nur Buchstaben, Leerzeichen oder das Zeichen '-' ein")
        return False

def fCheckTitle(userInput):
    mylist = "abcdefghijklmnopqrstuvwxyzöäüß -."
    if all(letter.lower() in mylist for letter in userInput):
        return True
    else:
        print("Geben Sie nur Buchstaben, Leerzeichen, Punkt oder das Zeichen '-' ein.")
        return False

def fCheckGeschlecht(userInput):
    if userInput == "m" or userInput == "w":
        return True
    else:
        print("Geben Sie nur 'm' oder 'w' ein.")
        return False

def fCheckEmail(userInput):
    if userInput == "":
        return True;
    mylist = "abcdefghijklmnopqrstuvwxyz .@"
    if isEmpty(userInput):
        return True
    count = 0
    for letter in userInput:
        if letter == "@":
            count = count + 1

    if count != 1:
        print("Die E-Mail-Adresse muss genau einen @-Symbol enthalten.")
        return False
    if userInput[0] == "@" or userInput[len(userInput)-1] == "@":
        print("Das Zeichen @ darf nicht an der ersten oder letzten Stelle in der E-Mail-Adresse stehen.")
        return False
    else:
        splitEmail = userInput.rsplit("@")
        if all('.' not in letter for letter in splitEmail[1]):
            print("Die E-Mail-Adresse muss mindestens einen Punkt nach dem @-Symbol enthalten.")
            return False
    if all(letter.lower() in mylist for letter in userInput):
        return True
    else:
        print("Geben Sie nur Buchstaben, Leerzeichen, Punkt oder das Zeichen '-' ein.")
        return False

def fChekPhone(userInput):
    mylist = "0123456789()-"
    if all(letter.lower() in mylist for letter in userInput):
        return True
    else:
        print("Bitte geben Sie nur Zahlen oder folgende Symbole: '-', '(',')' ein.")
        return False
def fCheckInsurance(userInput):
    if len(userInput) != 8:
        print("Die Sozialversicherungsnummer muss aus 8 Zahlen bestehen")
        return False
    else:
        for letter in userInput:
            if not letter.isnumeric():
                print("Bitte geben Sie nur Zahlen ein")
                return False
    return True

def fCheckStreet(userInput):
    mylist = "abcdefghijklmnopqrstuvwxyzöäüß -."
    if userInput[0] == " " or userInput[0] == "-" or userInput[0] == ".":
        print("An erster Stelle muss ein Buchstabe stehen.")
        return False
    else:
        if all(letter.lower() in mylist for letter in userInput):
            return True
        else:
            print("Geben Sie nur Buchstaben, Leerzeichen, Punkt oder das Zeichen '-' ein.")
            return False

def fCheckHaus(userInput):
    mylist = "abcdefghijklmnopqrstuvwxyz0123456789-/"
    if userInput[0] == " " or userInput[0] == "-" or userInput[0] == ".":
        print("An erster Stelle muss ein Buchstabe stehen.")
        return False
    else:
        if all(letter.lower() in mylist for letter in userInput):
            return True
        else:
            print("Geben Sie nur Buchstaben, Zahlen, oder folgende Symbole: '-', '/' ein.")
            return False


def fInputAndCheckStartDate(userInput):
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
