
import datetime

def isEmpty(userInput):
    if userInput == "":
        print("Dieses Feld darf nicht leer sein")
        return False
    else:
        return True
def fCheckName(userInput):
    mylist = "abcdefghijklmnopqrstuvwxyz -"
    if userInput[0] == " " or userInput[0] == "-":
        print("An erster Stelle muss ein Buchstabe stehen.")
        return False
    else:
        if all(letter.lower() in mylist for letter in userInput):
            return True
        else:
            print("Geben Sie nur Buchstaben, Leerzeichen oder das Zeichen '-' ein")
            return False

def fCheckTitle(userInput):
    mylist = "abcdefghijklmnopqrstuvwxyz -."
    if userInput[0] == " " or userInput[0] == "-" or userInput[0] == ".":
        print("An erster Stelle muss ein Buchstabe stehen.")
        return False
    if userInput[len(userInput)-1] != ".":
        print("An letzter Stelle muss nur ein Punkt stehen.")
        return False
    else:
        if all(letter.lower() in mylist for letter in userInput):
            return True
        else:
            print("Geben Sie nur Buchstaben, Leerzeichen, Punkt oder das Zeichen '-' ein.")
            return False

def fCheckEmail(userInput):

def fCheckData(personalData, userInput):
        if all('@' not in letter for letter in userInput):
            return False
        else:
            print("Geben Sie nur Buchstaben, Leerzeichen, Punkt oder das Zeichen '-' ein.")
            return False




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


def fInputAndCheckStartDate():
    while True:
        userInput = input(f"Arbeitet im Unternehmen seit (format: dd.mm.yyyy): ")
        dataList = userInput.rsplit(".")
        try:
            startDay = datetime.datetime(int(dataList[2]), int(dataList[1]), int(dataList[0]))
            print(startDay)
            if startDay <= datetime.datetime.now():
                return userInput
        except ValueError:
            print(f"Incorrect Date. Format: dd.mm.yyyy")
            continue
