
import tkinter as tk
from tkinter import messagebox
from EntryMenuGUI import *
from checkFunctions import *
from dataFunctions import *
from functionsGUI import firstLabelInFrame
from selectMenuGUI import *
from OutputMenuGUI import *

def changePerson(windowChangeRecord, key, entries, typeOfPerson):
    database = fileToDictionary(typeOfPerson)
    currentPersonDates = []
    for entry in entries:
        currentPersonDates.append(entry.get())
    database[key] = currentPersonDates
    writeDictionaryToFile(database, typeOfPerson)
    changeMenuGUI(windowChangeRecord, typeOfPerson)
def updateDataMenuGUI(key, windowChange, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    database = fileToDictionary(typeOfPerson)
    windowChangeRecord = tk.Tk()
    windowChange.destroy()
    startConfigure(windowChangeRecord)
    # ---------------------------------------------------------------------------------------------------------
    firstLabelInFrame(windowChangeRecord, f"Geben Sie die Daten des {translateTypeOfPerson(typeOfPerson)} an:")
    # ----------------------------------------------------------------------------------------------------------
    frameInput = tk.Frame(windowChangeRecord, relief="raised", borderwidth=4)
    frameInput.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    entries = []

    for i in range(len(atributesList)):
        label = tk.Label(frameInput, text=atributesList[i], bg="light gray")
        label.grid(row=i, column=0, padx=15, pady=10, sticky="ew")
        entry = tk.Entry(frameInput)
        entry.grid(row=i, column=1, padx=15, pady=10, sticky="ew")
        entries.append(entry)

    for i, entry in enumerate(entries,start=0):
        entry.insert(0,database[key][i])
# ----------------------------------------------------------------------------------------------------------
    frameButtons = tk.Frame(windowChangeRecord, relief="raised", borderwidth=4)
    frameButtons.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
    frameButtons.grid_columnconfigure(0, weight=1)
    frameButtons.grid_rowconfigure(0, weight=1)
    frameButtons.grid_rowconfigure(1, weight=1)
    frameButtons.grid_columnconfigure(1, weight=1)

    buttonSave = tk.Button(frameButtons, text="Daten Speichern", command=lambda: changePerson(windowChangeRecord,key, entries, typeOfPerson))
    buttonSave.grid(row=0, column=0, padx=15, pady=10, sticky="ew")

    buttonChangeMenu = tk.Button(frameButtons, text="Changemenü", command=lambda: changeMenuGUI(windowChangeRecord, typeOfPerson))
    buttonChangeMenu.grid(row=0, column=1, padx=15, pady=10, sticky="ew")

    buttonDelete = tk.Button(frameButtons, text="delete Dates", command=lambda: delEntries(entries))
    buttonDelete.grid(row=1, column=1, padx=15, pady=10, sticky="ew")

    pass
def changeMenuGUI(windowMain,typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    windowChange = tk.Tk()
    windowMain.destroy()
    startConfigure(windowChange)
# ----------------------------------------------------------------------------------
    firstLabelInFrame(windowChange,f"Geben Sie die Daten ein, nach denen Sie die {translateTypeOfPerson(typeOfPerson)} ändern möchten")
#-----------------------------------------------------------------------------------
# ------------------------Results+Buttons-----------------------------------------------------------
    frameResults = tk.Frame(windowChange, relief="raised", borderwidth=4)
    frameResults.grid(row=1, column=0, padx=8, pady=10, sticky="new")

    database = fileToDictionary(typeOfPerson)

    outputSelectionFrame(database, windowChange, frameResults, typeOfPerson)

    for row, key in enumerate(database.keys(), start=1):
        buttonEdit = tk.Button(frameResults, text="Edit", command=lambda k=key: updateDataMenuGUI(k, windowChange, typeOfPerson))
        buttonEdit.grid(row=row, column=len(atributesList)+2)
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
                       [menuItems[6],lambda: changeMenuGUI(windowMain,"Employee")],
                       [menuItems[7],lambda: changeMenuGUI("Visitor")],
                       [menuItems[8],lambda: printBirthdaysEmployeeGUI()],
                       [menuItems[9],lambda: closeDatabase()]]
    return mainMenuButtons


def mainmenuGUI():
    windowMain = tk.Tk()
    windowMain.title("Der Datenbank für Mitarbeiter*innen und Besucher*innen")
    startConfigure(windowMain)
# -----------------frame with first label
    firstLabelInFrame(windowMain,"Willkommen in der Datenbank!")

#-----------------frame with buttons
    frame2 = tk.Frame(windowMain, relief="raised", borderwidth=4)
    frame2.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    startConfigure(frame2)

    mainMenubuttons = getMainMenuButtons(getMainMenuItems(), windowMain)

    for i in range(len(mainMenubuttons)):
        frame = tk.Frame(frame2)
        frame.grid(row=i, column=0, padx=50, pady=10, sticky="ew")
        button = tk.Button(frame, text=mainMenubuttons[i][0], command=mainMenubuttons[i][1])
        button.pack()

    windowMain.mainloop()

