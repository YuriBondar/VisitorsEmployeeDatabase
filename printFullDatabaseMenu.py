import tkinter as tk

from dataFunctions import *
from functionsGUI import *


def printDatabase(database,windowMain,typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    windowPrint = tk.Tk()
    windowMain.destroy()
    startConfigure(windowPrint)
#----------------------------------------------------------------------
    infoFrame(windowPrint, f"{typeOfPerson}datenbank")
#----------------------------------------------------------------------
    frameResults = tk.Frame(windowPrint, relief="raised", borderwidth=4)
    frameResults.grid(row=1, column=0, padx=10, pady=10, sticky="new")
    for i in range(len(atributesList) + 1):
        frameResults.grid_columnconfigure(i, weight=1)

    outputSelectionFrame(database, windowPrint, frameResults, typeOfPerson)
# ----------------------------------------------------------------------
    frame3 = tk.Frame(windowPrint, relief="raised", borderwidth=4)
    frame3.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    buttonMainMenu = tk.Button(frame3, text="Hauptmenü", command=lambda: backToMainMenu(windowPrint))
    buttonMainMenu.grid(row=0, column=1, padx=15, pady=10, sticky="ew")

    windowPrint.mainloop()

def printFullDatabaseMenu(windowMain,typeOfPerson):
    database = fileToDictionary(typeOfPerson)
    printDatabase(database, windowMain, typeOfPerson)