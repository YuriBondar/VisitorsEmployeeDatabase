import csv

from databaseFunctions import *


if __name__ == "__main__":


    print("Willkommen in der Datenbank!")
    while True:
        print("Wählen die Option:")
        print("1. Neuen Eintrag für Besucher erstellen")
        print("2. Neuen Eintrag für Mitarbeiter erstellen")
        print("3. die Arbeit mit der Datenbank beenden")
        status = input()
        if status == "1":
            with open('Employees.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(fCreateNewEmployeeV2())
        elif status == "2":
            with open('Visitots.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(fCreateNewEmployeeV2())
        else:
            break
















