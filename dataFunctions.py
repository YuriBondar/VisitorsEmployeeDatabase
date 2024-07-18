import csv
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

def translateTypeOfPerson(typeOfPerson):
    if typeOfPerson == "Employee":
        return "Mitarbeiter"
    else:
        return "Besucher"

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

def getMainMenuItems():
    menuItems = ["Neuen Eintrag für Mitarbeiter*innen erstellen",
                 "Neuen Eintrag für Besucher*innen erstellen",
                 "Mitarbeiterinformationen suchen/anzeigen",
                 "Vollständige Mitarbeiterdatenbank anzeigen",
                 "Besucherinformationen suchen/anzeigen",
                 "Vollständige Besucherdatenbank anzeigen",
                 "Mitarbeiterinformationen ändern",
                 "Besucherinformationen ändern",
                 "Geburtstage der Mitarbeiter für diesen Monat anzeigen",
                 "Das Programm beenden"]
    return menuItems

def birthdaysEmployee():
    currentMonth = datetime.now().month
    nextMonth = (datetime.now() + relativedelta(month=1)).month
    database = fileToDictionary("Employee")
    birthdayList = []
    i = 0

    for person, value in database.items():
        birthdayDate = datetime.strptime(value[10], "%d.%m.%Y")
        if currentMonth == birthdayDate.month or nextMonth == birthdayDate.month:
            differenceDays = birthdayDate.day - datetime.now().day
            if differenceDays > 0:
                specialString = f"Bis zum Geburstag {differenceDays} Tage"
            elif differenceDays < 0:
                specialString = f"Der Geburstag ist {abs(differenceDays)} Tage her"
            else:
                specialString = "Der Geburstag ist heute!"
            birthdayList.append([value[0], value[1], value[10], specialString, differenceDays])

    birthdayList = sorted(birthdayList, key=lambda x: x[4])
    for person in birthdayList:
        del person[4]

    return birthdayList



#-------------------------------------------------------------------------------
#------------------Funktionen für die Arbeit mit Dataien------------------------
#-------------------------------------------------------------------------------
def writeDictionaryToFile(fullDictinary, typeOfPerson):
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

def addRecordtoFile(newRecord, typeOfPerson):
    if typeOfPerson == "Employee":
        fileName = "Employees.csv"
    else:
        fileName = "Visitors.csv"
    if not os.path.exists(fileName):
        print(f"Achtung, die Datenbank mit {typeOfPerson} wurde nicht gefunden. Es wird eine neue Mitarbeiterdatenbank erstellt.")
    with open(fileName, 'a', newline='') as file:
        writer = csv.writer(file)
        if fileName == "Employees.csv":
            writer.writerow(newRecord)
        else:
            writer.writerow(newRecord)