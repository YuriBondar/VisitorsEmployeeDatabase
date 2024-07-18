import tkinter as tk

from dataFunctions import *
from functionsGUI import *


# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# -------------------BIRTHDAY MENU-----------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

def birthdayListMenu(windowMain):
    typeOfPerson = "Employee"
    atributesList = chooseAtributesList(typeOfPerson)

    windowBirthday = tk.Tk()
    windowMain.destroy()
    startConfigure(windowBirthday)
# ---------------------------------------------------------------------------------------------------------
# ---------------- INFO FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    infoFrame(windowBirthday, f"Liste der Mitarbeiter, die in diesem oder nächstem Monat Geburtstag haben")
# ---------------------------------------------------------------------------------------------------------
# ----------------RESULTS FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    frameResults = tk.Frame(windowBirthday, relief="raised", borderwidth=4)
    frameResults.grid(row=1, column=0, padx=10, pady=10, sticky="new")

    birthdayList = birthdaysEmployee()
    headList = ["Name", "Vorname", "Geburtstag", ""]
    for i in range(len(headList)):
        label = tk.Label(frameResults, text=headList[i])
        label.grid(row=0, column=i, padx=10, pady=10, sticky="ew")
    for row, person in enumerate(birthdayList):
        for i in range(len(headList)):
            label = tk.Label(frameResults, text=person[i])
            label.grid(row=row+1, column=i, padx=10, pady=10, sticky="ew")


#---------------------------------------------------------------------------------------------------------
# ---------------- BUTTONS FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    frameButtons = tk.Frame(windowBirthday, relief="raised", borderwidth=4)
    frameButtons.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
    frameButtons.grid_columnconfigure(0, weight=1)
    frameButtons.grid_rowconfigure(0, weight=1)
    frameButtons.grid_rowconfigure(1, weight=1)
    frameButtons.grid_columnconfigure(1, weight=1)

    buttonMainMenu = tk.Button(frameButtons, text="Hauptmenü", command=lambda: backToMainMenu(windowBirthday))
    buttonMainMenu.grid(row=0, column=1, padx=15, pady=10, sticky="ew")
