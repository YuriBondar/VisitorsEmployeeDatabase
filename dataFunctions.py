import csv

#---------------------------------------------------
#--------konvertiert die Datei in Dictionary
#---------------------------------------------------
def fileToDictionary(typeOfPerson):
    if typeOfPerson == "Employee":
        fileName = "Employees.csv"
    else:
        fileName = "Visitors.csv"
    fullDictinary = {}
    typeOfPersonGer = translateTypeOfPerson(typeOfPerson)
    i = 0
    try:
        with open(fileName, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                i = i + 1
                fullDictinary[f"{typeOfPersonGer} {i}"] = list(row)
            return fullDictinary
    except Exception as e:
        print("Die Datenbank mit Ihren Mitarbeitern wurde nicht gefunden")
#-------------------------------------------------------------------------
#--------List mit Nummern ab 1 anzeigen, um verschiedene Menüs anzuzeigen
#-------------------------------------------------------------------------
def printList(listItems):
    i = 0
    for listItem in listItems:
        i = i + 1
        print(f"{i}. {listItem}")
    return i

def translateTypeOfPerson(typeOfPerson):
    if typeOfPerson == "Employee":
        return "Mitarbeiter"
    else:
        return "Besucher"
def printDictinary(dictinary, typeOfPerson):
    typeOfPersonGer = translateTypeOfPerson(typeOfPerson)
    print("---------------------------------------------------------------------------------------------------------------------")
    print(f"{typeOfPersonGer}: {chooseAtributesList(typeOfPerson)}")
    print("----------------------------------------------------------------------------------------------------------------------")
    for person, value in dictinary.items():
        print(f"{person} : {value}")
    print("----------------------------------------------------------------------------------------------------------------------")
    input("Eine beliebige Taste drücken")

def printFullDatabase(typeOfPerson):
    database = fileToDictionary(typeOfPerson)
    printDictinary(database, typeOfPerson)



def writeToFile(fullDictinary, typeOfPerson):
    if typeOfPerson == "Employee":
        fileName = "Employees.csv"
    else:
        fileName = "Visitors.csv"
    try:
        with open(fileName, 'w', newline='') as file:
            writer = csv.writer(file)
            for person in fullDictinary:
                writer.writerow(fullDictinary[person])
    except Exception as e:
        print("Die Datenbank mit Ihren Mitarbeitern wurde nicht gefunden")

#---------------------------------------------------------------------------

def chooseAtributesList(typeOfPerson):

    employeeAtributesList = ["Nachname",
                            "Vorname",
                            "Geschlecht",
                            "Title",
                            "Sozialversicherungsnummer",
                            "E-Mail",
                            "Telefonnummer",
                            "Ort",
                            "Straße",
                            "Hausnummer",
                            "Geburtsdatum"]

    visitorAtributesList = ["Nachname",
                            "Vorname",
                            "E-Mail",
                            "Telefonnummer",
                            "Verantwortlicher Manager",
                            "Tag und Zeit des Besuchs"]

    if typeOfPerson == "Employee":
        return employeeAtributesList
    if typeOfPerson == "Visitor":
        return visitorAtributesList