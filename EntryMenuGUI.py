from tkinter import messagebox
import tk
from checkFunctions import *
from dataFunctions import *
from mainmenuGUI import *
from functionsGUI import *


def delEntries(entries):
    for entry in entries:
        entry.delete(0,tk.END)

def entryPerson(entries, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    newPerson = []
    for entry in entries:
        newPerson.append(entry.get())
    for i in range(len(newPerson)-1):
        if checkData(i+1, newPerson[i], typeOfPerson) is not True:
            errorMessage = checkData(i+1, newPerson[i], typeOfPerson)
            currentPerson = atributesList[i]
            messagebox.showerror("Error", f" Field {currentPerson} : {errorMessage}")
            return

    addRecordtoFile(newPerson, typeOfPerson)
    messagebox.showinfo("Dates are saved succesful",)
    delEntries(entries)

def addNewRecordGUI(windowMain, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    windowAdd = tk.Tk()
    windowMain.destroy()
    startConfigure(windowAdd)
#---------------------------------------------------------------------------------------------------------
    infoFrame(windowAdd, f"Geben Sie die Daten des {translateTypeOfPerson(typeOfPerson)} an:")
#----------------------------------------------------------------------------------------------------------
    frameInput = tk.Frame(windowAdd, relief="raised", borderwidth=4)
    frameInput.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    entries = []

    for i in range(len(atributesList)):
        label = tk.Label(frameInput, text=atributesList[i], bg="light gray")
        label.grid(row=i, column=0, padx=15, pady=10, sticky="ew")
        entry = tk.Entry(frameInput)
        entry.grid(row=i, column=1, padx=15, pady=10, sticky="ew")
        entries.append(entry)

# ----------------------------------------------------------------------------------------------------------
    frameButtons = tk.Frame(windowAdd, relief="raised", borderwidth=4)
    frameButtons.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
    frameButtons.grid_columnconfigure(0, weight=1)
    frameButtons.grid_rowconfigure(0, weight=1)
    frameButtons.grid_rowconfigure(1, weight=1)
    frameButtons.grid_columnconfigure(1, weight=1)


    buttonSave = tk.Button(frameButtons, text="Daten Speichern", command=lambda: entryPerson(entries,typeOfPerson))
    buttonSave.grid(row=0, column=0, padx=15, pady=10, sticky="ew")

    buttonMainMenu = tk.Button(frameButtons, text="Hauptmenü", command=lambda: backToMainMenu(windowAdd))
    buttonMainMenu.grid(row=0, column=1, padx=15, pady=10, sticky="ew")

    buttonDelete = tk.Button(frameButtons, text="delete Dates", command=lambda: delEntries(entries))
    buttonDelete.grid(row=1, column=1, padx=15, pady=10, sticky="ew")

    windowAdd.mainloop()