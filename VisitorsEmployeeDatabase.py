import csv

from databaseFunctions import *


if __name__ == "__main__":

    employeesList = []
    visitorsList = []

    print("Welcome to database!")
    while True:
        print("Type 'v' to create new record for visitor")
        print("Type 'e' to create new record for employee")
        status = input("Type 'f' to finish working with database ")
        if status == "e":
            with open('Employees.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(fCreateNewEmployeeV2())
        elif status == "v":
            with open('Visitots.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(fCreateNewEmployeeV2())
            if isEmployeeInDatabase():
                fAddVisitor()
            else:
                fcorrectVisitor()
        else:
            break

    pass














