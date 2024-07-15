import tkinter as tk

from dataFunctions import getMainMenuItems, chooseAtributesList


def addNewRecordGUI(typeOfPerson):
    AtributesList = chooseAtributesList(typeOfPerson)
    window = tk.Tk()

    label_frame = tk.Frame(window)
    pass

def selectRecordsGUI(typeOfPerson):
    pass

def printFullDatabaseGUI(typeOfPerson):
    pass
def changeRecordsGUI(typeOfPerson):
    pass

def printBirthdaysEmployeeGUI():
    pass

def closeDatabase():
    pass


def getMainMenuButtons(menuItems):
    mainMenuButtons = [[menuItems[0],addNewRecordGUI("Employee")],
                       [menuItems[1],addNewRecordGUI("Visitor")],
                       [menuItems[2],selectRecordsGUI("Employee")],
                       [menuItems[3],printFullDatabaseGUI("Employee")],
                       [menuItems[4],selectRecordsGUI("Visitor")],
                       [menuItems[5],printFullDatabaseGUI("Employee")],
                       [menuItems[6],changeRecordsGUI("Employee")],
                       [menuItems[7],changeRecordsGUI("Visitor")],
                       [menuItems[8],printBirthdaysEmployeeGUI()],
                       [menuItems[9],closeDatabase()]]
    return mainMenuButtons


def mainmenuGUI():
    window = tk.Tk()
    window.title("Der Datenbank für Mitarbeiter*innen und Besucher*innen")

    label_frame1 = tk.Frame(window)
    label_frame1.grid(row=0, column=0, pady=10, sticky="ew")

    label = tk.Label(label_frame1, text="Willkommen in der Datenbank!")
    #label.pack(padx=20, anchor="w")
    label.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
    #label_frame1.grid_columnconfigure(0, weight=1)

    label_frame2 = tk.Frame(window)
    label_frame2.grid(row=1, column=0, pady=10, sticky="ew")

    label = tk.Label(label_frame2, text="Wählen die Option:")
    label.pack(padx=20, anchor="w")

    mainMenubuttons = getMainMenuButtons(getMainMenuItems())

    for i in range(len(mainMenubuttons)):
        frame = tk.Frame(window)
        frame.grid(row=i+2, column=0, padx=100, pady=10)
        button = tk.Button(frame, text = mainMenubuttons[i][0], command = mainMenubuttons[i][1])
        button.pack()

    window.mainloop()

