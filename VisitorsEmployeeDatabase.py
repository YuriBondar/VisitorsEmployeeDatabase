


from databaseFunctions import *


if __name__ == "__main__":

    employeesPositions = (
    "Status: Mitarbeiter*inn oder Besucher*inn",
    "Nachname",
    "Vorname",
    "Title"
    "Telefonnummer",
    "E-Mail",
    "Sozialversicherungsnummer",
    "Arbeitet im Unternehmen seit:",
    )

    visitorsPositions = (
        "Status: Mitarbeiter*inn oder Besucher*inn",
        "Nachname",
        "Vorname",
        "Telefonnummer",
        "E-Mail",
        "Tag und Zeit des Besuchs"
        "Verantwortlicher Manager")

    employee = ["", "", "", 0, "", "", "", ""]
    visitor = ["", "", "", 0, "", "", ""]
    employeesList = []
    visitorsList = []

    print("Welcome to database!")
    while True:
        print("Type 'v' to create new record for visitor")
        print("Type 'e' to create new record for employee")
        status = input("Type 'f' to finish working with database ")
        if status == "e":
                fCreateNewEmployee()
        elif status == "v":
            fCreateNewVisitor()
            if isEmployeeInDatabase():
                fAddVisitor()
            else:
                fcorrectVisitor()
        else:
            break

    pass














