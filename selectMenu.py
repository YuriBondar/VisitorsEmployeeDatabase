from tkinter import messagebox

from entryMenu import *
from printFullDatabaseMenu import *
from dataFunctions import *
from functionsGUI import *

def select(entries, frameResults, windowSelect, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    for widget in frameResults.winfo_children():
        widget.destroy()

    database = fileToDictionary(typeOfPerson)
    filterList = []
    resultSelection = {}

    for entry in entries:
        if entry.get() != "":
            filterList.append(entry.get())
    if not filterList:
        messagebox.showerror("Error", f" Suchliste ist leer")
        return

    for index, entry in enumerate(entries):
        if entry.get() != "":
            if checkData(index+1, entry.get(), typeOfPerson) is not True:
                errorMessage = checkData(index+1, entry.get(), typeOfPerson)
                currentPerson = atributesList[index]
                messagebox.showerror("Error", f" Field {currentPerson} : {errorMessage}")
                return

    for person, dates in database.items():
        if all(elem in dates for elem in filterList):
            resultSelection.update({person: dates})

    outputSelectionFrame(resultSelection, windowSelect, frameResults, typeOfPerson)
    return resultSelection

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# -------------------SELECT MENU-----------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

def selectMenu(windowMain, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)

    windowSelect = tk.Tk()
    windowMain.destroy()
    startConfigure(windowSelect)
# ---------------------------------------------------------------------------------------------------------
# ---------------- INFO FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    infoFrame(windowSelect, f"Geben Sie die Daten ein, nach denen Sie die {translateTypeOfPerson(typeOfPerson)} "
                            f"filtern möchten")
# ---------------------------------------------------------------------------------------------------------
# ---------------- INPUT FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    frameAttributs = tk.Frame(windowSelect, relief="raised", borderwidth=4)
    frameAttributs.grid(row=1, column=0, padx=8, pady=10, sticky="ew")

    label = tk.Label(frameAttributs, text=translateTypeOfPerson(typeOfPerson))
    label.grid(row=0, column=0, padx=10, pady=8, sticky="ew")

    entries = []

    for i in range(len(atributesList)):
        label = tk.Label(frameAttributs, text=atributesList[i])
        label.grid(row=0, column=i+1, padx=8, pady=10, sticky="ew")
        entry = tk.Entry(frameAttributs, width=17)
        entry.grid(row=1, column=i+1, padx=8, pady=10, sticky="ew")
        entries.append(entry)
# ---------------------------------------------------------------------------------------------------------
# ---------------- RESULTS FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    frameResults = tk.Frame(windowSelect, relief="raised", borderwidth=4)
    frameResults.grid(row=2, column=0, padx=8, pady=10, sticky="new")
    for i in range(len(atributesList)+1):
        frameResults.grid_columnconfigure(i, weight=1)


# ---------------------------------------------------------------------------------------------------------
# ---------------- BUTTONS FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    frameButtons = tk.Frame(windowSelect, relief="raised", borderwidth=4)
    frameButtons.grid(row=3, column=0, padx=5, pady=10, sticky="ew")

    buttonSelect = tk.Button(frameButtons, text="Daten Filtern",
                             command=lambda: select(entries, frameResults, windowSelect, typeOfPerson))
    buttonSelect.grid(row=0, column=0, padx=15, pady=10, sticky="ew")

    buttonMainMenu = tk.Button(frameButtons, text="Hauptmenü", command=lambda: backToMainMenu(windowSelect))
    buttonMainMenu.grid(row=0, column=1, padx=15, pady=10, sticky="ew")




