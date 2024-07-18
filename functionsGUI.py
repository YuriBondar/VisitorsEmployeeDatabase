import tkinter as tk
from tkinter import messagebox

from checkFunctions import checkData
from dataFunctions import *


#-------- go back to main menu from other menus------------
#----------------------------------------------------------
def backToMainMenu(window):
    window.destroy()
    from mainMenu import mainMenu
    mainMenu()

#--------info frame (usual first in every window)------------
#------------------------------------------------------------
def infoFrame(window, text):
    frame1 = tk.Frame(window, relief="raised", borderwidth=4)
    frame1.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    label = tk.Label(frame1, text=text, bg="light gray")
    label.pack(pady=10, expand=True)

#--------configuration for frame----------------------------
#------------------------------------------------------------
def startConfigure(window):
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)


def fillInInputFrameEntryMenu(frameInput, entries, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    for i in range(len(atributesList)):
        label = tk.Label(frameInput, text=atributesList[i], bg="light gray")
        label.grid(row=i, column=0, padx=15, pady=10, sticky="ew")
        entry = tk.Entry(frameInput)
        entry.grid(row=i, column=1, padx=15, pady=10, sticky="ew")
        entries.append(entry)

    return entries

def delEntries(entries):
    for entry in entries:
        entry.delete(0, tk.END)

def checkPerson(person, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    for i in range(len(person)-1):
        if checkData(i+1, person[i], typeOfPerson) is not True:
            errorMessage = checkData(i+1, person[i], typeOfPerson)
            currentPerson = atributesList[i]
            messagebox.showerror("Error", f" Field {currentPerson} : {errorMessage}")
            return False
    else:
        return True

def outputSelectionFrame(database, window, frame, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    if database == {}:
        label = tk.Label(frame, text="No match")
        label.grid(row=0, column=0, padx=15, pady=10, sticky="ew")
    else:
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