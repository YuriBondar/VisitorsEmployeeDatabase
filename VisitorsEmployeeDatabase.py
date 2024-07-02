
if __name__ == "__main__":

    employeesPositions = (
    "Status: Mitarbeiter*inn oder Besucher*inn",
    "Nachname",
    "Vorname",
    "Telefonnummer",
    "E-Mail",
    "Sozialversicherungsnummer",
    "Arbeitet im Unternehmen seit:",
    "Position")

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
    while True
        print("Type 'v' to create new record for visitor")
        print("Type 'e' to create new record for employee")
        status = input("Type 'e' to create new record for employee: ")
        if status == "e":
                fCreateNewEmployee()
        if status == "v":
                fCreateNewVisitor()

            if isEmployeeIndatabase():
                fAddVisitor()
                break
            else:
                fcorrectVisitor()
                break
        else:
            pass














