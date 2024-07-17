import tkinter as tk

from dataFunctions import *
from functionsGUI import *

def outputSelectionFrame(database, window, frame, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)

    label = tk.Label(frame, text=translateTypeOfPerson(typeOfPerson))
    label.grid(row=0, column=0, padx=15, pady=10, sticky="ew")

    for i in range(len(atributesList)):
        label = tk.Label(frame, text=atributesList[i])
        label.grid(row=0, column=i+1, padx=10, pady=10, sticky="ew")
    i = 0
    for person in database.keys():
        i = i + 1
        label = tk.Label(frame, text=person)
        label.grid(row=i, column=0, padx=10, pady=10, sticky="ew")
        for j in range(len(atributesList)):
            label = tk.Label(frame, text=database[person][j])
            label.grid(row=i, column=j+1, padx=10, pady=10, sticky="ew")

def printDatabaseGUI(database,windowMain,typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    windowPrint = tk.Tk()
    windowMain.destroy()
    startConfigure(windowPrint)
#----------------------------------------------------------------------
    firstLabelInFrame(windowPrint, f"{typeOfPerson}datenbank")
#----------------------------------------------------------------------
    frameAttributs = tk.Frame(windowPrint, relief="raised", borderwidth=4)
    frameAttributs.grid(row=1, column=0, padx=10, pady=10, sticky="new")

    outputSelectionFrame(database, windowPrint, frameAttributs, typeOfPerson)
# ----------------------------------------------------------------------
    frame3 = tk.Frame(windowPrint, relief="raised", borderwidth=4)
    frame3.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    buttonMainMenu = tk.Button(frame3, text="Hauptmenü", command=lambda: backToMainMenu(windowPrint))
    buttonMainMenu.grid(row=0, column=1, padx=15, pady=10, sticky="ew")

    windowPrint.mainloop()

def printFullDatabaseGUI(windowMain,typeOfPerson):
    database = fileToDictionary(typeOfPerson)
    printDatabaseGUI(database, windowMain, typeOfPerson)