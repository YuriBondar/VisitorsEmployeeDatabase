from EntryMenuGUI import *
from OutputMenuGUI import *
from checkFunctions import *
from dataFunctions import *
from functionsGUI import firstLabelInFrame

def select(entries, frame, windowSelect, typeOfPerson):
    for widget in frame.winfo_children():
        widget.destroy()
    # frame = tk.Frame(windowSelect, relief="raised", borderwidth=4)
    # frame.grid(row=2, column=0, padx=8, pady=10, sticky="new")
    database = fileToDictionary(typeOfPerson)
    resultSelection = {}
    filterList = []

    for entry in entries:
        if entry.get() != "":
            filterList.append(entry.get())

    for person, dates in database.items():
        if all(elem in dates for elem in filterList):
            resultSelection.update({person: dates})

    outputSelectionFrame(resultSelection, windowSelect, frame, typeOfPerson)


def selectMenuGUI(windowMain, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    windowSelect = tk.Tk()
    windowMain.destroy()
    startConfigure(windowSelect)
#----------------------------------------------------------------------------------
    firstLabelInFrame(windowSelect, f"Geben Sie die Daten ein, nach denen Sie die {translateTypeOfPerson(typeOfPerson)} filtern möchten")
#----------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------------------------
    frameResults = tk.Frame(windowSelect, relief="raised", borderwidth=4)
    frameResults.grid(row=2, column=0, padx=8, pady=10, sticky="new")

    # ------------------------------------------------------------------------------------------------
    frameButtons = tk.Frame(windowSelect, relief="raised", borderwidth=4)
    frameButtons.grid(row=3, column=0, padx=5, pady=10, sticky="ew")

    buttonSelect = tk.Button(frameButtons, text="Daten Filtern", command=lambda: select(entries, frameResults, windowSelect, typeOfPerson))
    buttonSelect.grid(row=0, column=0, padx=15, pady=10, sticky="ew")

    buttonMainMenu = tk.Button(frameButtons, text="Hauptmenü", command=lambda: backToMainMenu(windowSelect))
    buttonMainMenu.grid(row=0, column=1, padx=15, pady=10, sticky="ew")
