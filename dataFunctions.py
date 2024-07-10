import csv

#---------------------------------------------------
#--------konvertiert die Datei in Dictionary
#---------------------------------------------------
def fileToDictionary(fileName):
    employeeDictinary = {}
    i = 0
    try:
        with open(fileName, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                i = i + 1
                employeeDictinary[f"Mitarbeiter {i}"] = list(row)
            return employeeDictinary
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
#-------------------------------------------------------------------------
#--------Datai anzeigen
#-------------------------------------------------------------------------
def printDatabase(typeOfPerson):
    if typeOfPerson == "Employee":
        fileName = "Employees.csv"
    else:
        fileName = "Visitors.csv"
    try:
        with open(fileName, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except Exception as e:
        print("Die Datenbank mit Ihren Mitarbeitern wurde nicht gefunden")

#---------------------------------------------------------------------------

def chooseAtributesList(status):
    employeeAtributesList = ["Status",
                            "Nachname",
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


    besucherAtributesList = ["Status",
                            "Nachname",
                            "Vorname",
                            "E-Mail",
                            "Telefonnummer",
                            "Verantwortlicher Manager",
                            "Tag und Zeit des Besuchs"]

    if status == "Employee":
        return employeeAtributesList
    if status == "Visitor":
        return besucherAtributesList