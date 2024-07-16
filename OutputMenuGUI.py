import tkinter as tk

from dataFunctions import *
from functionsGUI import *

def printDatabaseGUI(database,windowMain,typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    windowPrint = tk.Tk()
    windowMain.destroy()
    windowPrint.grid_columnconfigure(0, weight=1)
    windowPrint.grid_rowconfigure(0, weight=1)
    windowPrint.grid_rowconfigure(1, weight=1)
#----------------------------------------------------------------------
    firstLabelInFrame(windowPrint, f"{typeOfPerson}datenbank")
#----------------------------------------------------------------------
    frameAttributs = tk.Frame(windowPrint, relief="raised", borderwidth=4)
    frameAttributs.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    label = tk.Label(frameAttributs, text=translateTypeOfPerson(typeOfPerson))
    label.grid(row=0, column=0, padx=15, pady=10, sticky="ew")

    for i in range(len(atributesList)):
        label = tk.Label(frameAttributs, text=atributesList[i])
        label.grid(row=0, column=i+1, padx=10, pady=10, sticky="ew")
    i = 0
    for person in database.keys():
        i = i + 1
        label = tk.Label(frameAttributs, text=person)
        label.grid(row=i, column=0, padx=10, pady=10, sticky="ew")
        for j in range(len(atributesList)):
            label = tk.Label(frameAttributs, text=database[person][j])
            label.grid(row=i, column=j+1, padx=10, pady=10, sticky="ew")
# ----------------------------------------------------------------------
    frame3 = tk.Frame(windowPrint, relief="raised", borderwidth=4)
    frame3.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    buttonMainMenu = tk.Button(frame3, text="Back to Main Menu", command=lambda: backToMainMenu(windowPrint))
    buttonMainMenu.grid(row=0, column=1, padx=15, pady=10, sticky="ew")

    windowPrint.mainloop()

def printFullDatabaseGUI(windowMain,typeOfPerson):
    database = fileToDictionary(typeOfPerson)
    printDatabaseGUI(database, windowMain, typeOfPerson)