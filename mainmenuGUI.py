import tkinter as tk
from tkinter import messagebox

from EntryMenuGUI import *
from OutputMenuGUI import *
from checkFunctions import *
from dataFunctions import *
from functionsGUI import firstLabelInFrame

def select(entries, typeOfPerson):
    pass


def selectMenuGUI(windowMain, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    windowSelect = tk.Tk()
    windowMain.destroy()
    windowSelect.grid_columnconfigure(0, weight=1)
    windowSelect.grid_rowconfigure(0, weight=1)
    windowSelect.grid_rowconfigure(1, weight=1)
#----------------------------------------------------------------------------------
    firstLabelInFrame(windowSelect, f"Geben Sie die Daten ein, nach denen Sie die {translateTypeOfPerson(typeOfPerson)} filtern möchten")
#----------------------------------------------------------------------------------
    frameAttributs = tk.Frame(windowSelect, relief="raised", borderwidth=4)
    frameAttributs.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

    label = tk.Label(frameAttributs, text=translateTypeOfPerson(typeOfPerson))
    label.grid(row=0, column=0, padx=5, pady=10, sticky="ew")

    entries = []

    for i in range(len(atributesList)):
        label = tk.Label(frameAttributs, text=atributesList[i])
        label.grid(row=0, column=i+1, padx=7, pady=10, sticky="ew")
        entry = tk.Entry(frameAttributs, width=18)
        entry.grid(row=1, column=i+1, padx=7, pady=10, sticky="ew")
        entries.append(entry)

    frameButtons = tk.Frame(windowSelect, relief="raised", borderwidth=4)
    frameButtons.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

    buttonSelect = tk.Button(frameButtons, text="Daten Speichern", command=lambda: select(entries, typeOfPerson))
    buttonSelect.grid(row=0, column=0, padx=15, pady=10, sticky="ew")

    buttonMainMenu = tk.Button(frameButtons, text="Back to Main Menu", command=lambda: backToMainMenu(windowSelect))
    buttonMainMenu.grid(row=0, column=1, padx=15, pady=10, sticky="ew")

def changeRecordsGUI(typeOfPerson):
    pass

def printBirthdaysEmployeeGUI():
    pass

def closeDatabase():
    pass
#-----------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#---------------------------------------main menu------------------------------------------------
def getMainMenuButtons(menuItems, windowMain):
    mainMenuButtons = [[menuItems[0],lambda: addNewRecordGUI(windowMain, "Employee")],
                       [menuItems[1],lambda: addNewRecordGUI(windowMain,"Visitor")],
                       [menuItems[2],lambda: selectMenuGUI(windowMain, "Employee")],
                       [menuItems[3],lambda: printFullDatabaseGUI(windowMain,"Employee")],
                       [menuItems[4],lambda: selectMenuGUI(windowMain,"Visitor")],
                       [menuItems[5],lambda: printFullDatabaseGUI(windowMain,"Visitor")],
                       [menuItems[6],lambda: changeRecordsGUI("Employee")],
                       [menuItems[7],lambda: changeRecordsGUI("Visitor")],
                       [menuItems[8],lambda: printBirthdaysEmployeeGUI()],
                       [menuItems[9],lambda: closeDatabase()]]
    return mainMenuButtons


def mainmenuGUI():
    windowMain = tk.Tk()
    windowMain.title("Der Datenbank für Mitarbeiter*innen und Besucher*innen")
    windowMain.grid_columnconfigure(0, weight=1)
    windowMain.grid_rowconfigure(0, weight=1)
    windowMain.grid_rowconfigure(1, weight=1)
# -----------------frame with first label
    firstLabelInFrame(windowMain,"Willkommen in der Datenbank!")

#-----------------frame with buttons
    frame2 = tk.Frame(windowMain, relief="raised", borderwidth=4)
    frame2.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    frame2.grid_rowconfigure(0, weight=1)
    frame2.grid_columnconfigure(0, weight=1)

    mainMenubuttons = getMainMenuButtons(getMainMenuItems(), windowMain)

    for i in range(len(mainMenubuttons)):
        frame = tk.Frame(frame2)
        frame.grid(row=i, column=0, padx=50, pady=10, sticky="ew")
        button = tk.Button(frame, text=mainMenubuttons[i][0], command=mainMenubuttons[i][1])
        button.pack()

    windowMain.mainloop()

