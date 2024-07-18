
from tkinter import messagebox
import tkinter as tk

from dataFunctions import *
from functionsGUI import *

def entryPerson(entries, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)

    newPerson = []
    for entry in entries:
        newPerson.append(entry.get())
    if not checkPerson(newPerson, typeOfPerson):
        return

    addRecordtoFile(newPerson, typeOfPerson)
    messagebox.showinfo("Meldung", "Daten wurden erfolgreich gespeichert",)
    delEntries(entries)
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# -------------------ENTRY MENU-----------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
def entryMenu(windowMain, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    windowMain.destroy()
    windowAdd = tk.Tk()
    windowAdd.geometry("500x700+500+80")
    windowAdd.title("Der Datenbank für Mitarbeiter*innen und Besucher*innen")
    startConfigure(windowAdd)
# ---------------------------------------------------------------------------------------------------------
# ---------------- INFO FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    infoFrame(windowAdd, f"Geben Sie die Daten des {translateTypeOfPerson(typeOfPerson)} an:")
# ---------------------------------------------------------------------------------------------------------
# ---------------- INPUT FRAME-----------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    frameInput = tk.Frame(windowAdd, relief="raised", borderwidth=4)
    frameInput.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    frameInput.grid_columnconfigure(0, weight=1)
    frameInput.grid_columnconfigure(1, weight=1)

    entries = []
    entries = fillInInputFrameEntryMenu(frameInput, entries, typeOfPerson)
# ---------------------------------------------------------------------------------------------------------
# -----------------BUTTONS FRAME-----------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    frameButtons = tk.Frame(windowAdd, relief="raised", borderwidth=4)
    frameButtons.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
    frameButtons.grid_columnconfigure(0, weight=1)
    frameButtons.grid_rowconfigure(0, weight=1)
    frameButtons.grid_rowconfigure(1, weight=1)
    frameButtons.grid_columnconfigure(1, weight=1)

    buttonSave = tk.Button(frameButtons, text="Daten Speichern", command=lambda: entryPerson(entries, typeOfPerson))
    buttonSave.grid(row=0, column=0, padx=15, pady=10, sticky="ew")

    buttonMainMenu = tk.Button(frameButtons, text="Hauptmenü", command=lambda: backToMainMenu(windowAdd))
    buttonMainMenu.grid(row=0, column=1, padx=15, pady=10, sticky="ew")

    buttonDelete = tk.Button(frameButtons, text="Daten löschen", command=lambda: delEntries(entries))
    buttonDelete.grid(row=1, column=1, padx=15, pady=10, sticky="ew")

    windowAdd.mainloop()