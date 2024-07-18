import tkinter as tk

from printFullDatabaseMenu import *
from dataFunctions import *
from functionsGUI import *
from selectMenu import *

def changePerson(windowChangeRecord, key, entries, typeOfPerson):
    database = fileToDictionary(typeOfPerson)
    currentPersonDates = []
    for entry in entries:
        currentPersonDates.append(entry.get())

    if not checkPerson(currentPersonDates, typeOfPerson):
        return

    database[key] = currentPersonDates
    messagebox.showinfo("Meldung", "Daten wurden erfolgreich verändert", )
    writeDictionaryToFile(database, typeOfPerson)
    changeMenuGUI(windowChangeRecord, typeOfPerson)
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------- UPDATE MENU------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
def updateDataMenuGUI(key, windowChange, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    database = fileToDictionary(typeOfPerson)

    windowChangeRecord = tk.Tk()
    windowChange.destroy()
    startConfigure(windowChangeRecord)
# ---------------------------------------------------------------------------------------------------------
# ---------------- INFO FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    infoFrame(windowChangeRecord, f"Geben Sie die Daten des {translateTypeOfPerson(typeOfPerson)} an:")
# ---------------------------------------------------------------------------------------------------------
# ---------------- INPUT FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
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
# ---------------------------------------------------------------------------------------------------------
# ---------------- BUTTONS FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    frameButtons = tk.Frame(windowChangeRecord, relief="raised", borderwidth=4)
    frameButtons.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
    frameButtons.grid_columnconfigure(0, weight=1)
    frameButtons.grid_rowconfigure(0, weight=1)
    frameButtons.grid_rowconfigure(1, weight=1)
    frameButtons.grid_columnconfigure(1, weight=1)

    buttonSave = tk.Button(frameButtons, text="Daten Speichern",
                           command=lambda: changePerson(windowChangeRecord,key, entries, typeOfPerson))
    buttonSave.grid(row=0, column=0, padx=15, pady=10, sticky="ew")

    buttonChangeMenu = tk.Button(frameButtons, text="Changemenü", #
                                 command=lambda: changeMenuGUI(windowChangeRecord, typeOfPerson))
    buttonChangeMenu.grid(row=0, column=1, padx=15, pady=10, sticky="ew")

    buttonDelete = tk.Button(frameButtons, text="Daten löschen", command=lambda: delEntries(entries))
    buttonDelete.grid(row=1, column=1, padx=15, pady=10, sticky="ew")
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------- CHANGE MENU------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
def selectInChangeMenu(entries, frameResults, windowChange, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    resultselection = select(entries, frameResults, windowChange, typeOfPerson)
    for row, key in enumerate(resultselection.keys(), start=1):
        buttonEdit = tk.Button(frameResults, text="Verändern",
                               command=lambda k=key: updateDataMenuGUI(k, windowChange, typeOfPerson))
        buttonEdit.grid(row=row, column=len(atributesList)+2, padx=8, pady=10, sticky="new")

def changeMenuGUI(window, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)

    database = fileToDictionary(typeOfPerson)

    windowChange = tk.Tk()
    window.destroy()
    startConfigure(windowChange)
# ---------------------------------------------------------------------------------------------------------
# ---------------- INFO FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

    infoFrame(windowChange,f"Geben Sie die Daten ein, nach denen Sie die"
                           f" {translateTypeOfPerson(typeOfPerson)} ändern möchten")
# ---------------------------------------------------------------------------------------------------------
# ---------------- SELECT FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    frameAttributs = tk.Frame(windowChange, relief="raised", borderwidth=4)
    frameAttributs.grid(row=1, column=0, padx=8, pady=10, sticky="ew")

    label = tk.Label(frameAttributs, text=translateTypeOfPerson(typeOfPerson))
    label.grid(row=0, column=0, padx=10, pady=8, sticky="ew")

    entries = []

    for i in range(len(atributesList)):
        label = tk.Label(frameAttributs, text=atributesList[i])
        label.grid(row=0, column=i + 1, padx=8, pady=10, sticky="ew")
        entry = tk.Entry(frameAttributs, width=17)
        entry.grid(row=1, column=i + 1, padx=8, pady=10, sticky="ew")
        entries.append(entry)
# ---------------------------------------------------------------------------------------------------------
# ---------------- BUTTONS FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    frameButtons = tk.Frame(windowChange, relief="raised", borderwidth=4)
    frameButtons.grid(row=2, column=0, padx=5, pady=10, sticky="ew")

    buttonSelect = tk.Button(frameButtons, text="Daten Filtern",
                             command=lambda: selectInChangeMenu(entries, frameResults, windowChange, typeOfPerson))
    buttonSelect.grid(row=0, column=0, padx=15, pady=10, sticky="ew")

    buttonMainMenu = tk.Button(frameButtons, text="Hauptmenü", command=lambda: backToMainMenu(windowChange))
    buttonMainMenu.grid(row=0, column=1, padx=15, pady=10, sticky="ew")
# ---------------------------------------------------------------------------------------------------------
# ---------------- RESULTS FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    frameResults = tk.Frame(windowChange, relief="raised", borderwidth=4)
    frameResults.grid(row=3, column=0, padx=8, pady=10, sticky="new")
    for i in range(len(atributesList)+1):
        frameResults.grid_columnconfigure(i, weight=1)


    outputSelectionFrame(database, windowChange, frameResults, typeOfPerson)

    for row, key in enumerate(database.keys(), start=1):
        buttonEdit = tk.Button(frameResults, text="Verändern",
                               command=lambda k=key: updateDataMenuGUI(k, windowChange, typeOfPerson))
        buttonEdit.grid(row=row, column=len(atributesList)+2, padx=8, pady=10, sticky="new")
    pass