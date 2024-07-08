import csv

from databaseFunctions import *
from menu import *

#----------------------main-----------------------------------------

if __name__ == "__main__":


    fMenu()


    print("Willkommen in der Datenbank!")
    while True:
        print("Wählen die Option:")
        print("1. Neuen Eintrag für Mitarbeiter*innen erstellen")
        print("2. Neuen Eintrag für Besucher*innen erstellen")
        print("3. Die Liste der Mitarbeiter*innen anzeigen")
        print("4. Die Liste der Besucher*innen anzeigen")
        print("5. die Arbeit mit der Datenbank beenden")
        status = input()
        if status == "1":
            with open('Employees.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(fCreateNewEmployeeV2())
        if status == "2":
            with open('Visitors.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(fCreateNewEmployeeV2())
        if status == "3":
            with open('Employees.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        if status == "4":
            with open('Visitors.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        if status == "5":
            break
















