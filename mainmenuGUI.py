import tkinter as tk

from checkFunctions import *
from dataFunctions import *
from tkinter import messagebox

def firstLabelInFrame(window, text):
    frame1 = tk.Frame(window, relief = "raised", borderwidth=4)
    frame1.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    label = tk.Label(frame1, text=text, bg="light gray")
    label.pack(pady=10, expand=True)

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
    for entry in entries:
        entry.delete(0,tk.END)

def addNewRecordGUI(windowMain, typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    windowAdd = tk.Tk()
    windowMain.destroy()
    windowAdd.grid_columnconfigure(0, weight=1)
    windowAdd.grid_rowconfigure(0, weight=1)
    windowAdd.grid_rowconfigure(1, weight=1)
#---------------------------------------------------------------------------------------------------------
    firstLabelInFrame(windowAdd, f"Geben Sie die Daten des {translateTypeOfPerson(typeOfPerson)} an:")
#----------------------------------------------------------------------------------------------------------
    frame2 = tk.Frame(windowAdd, relief="raised", borderwidth=4)
    frame2.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    entries = []

    for i in range(len(atributesList)):
        label = tk.Label(frame2, text=atributesList[i], bg="light gray")
        label.grid(row=i, column=0, padx=15, pady=10, sticky="ew")
        entry = tk.Entry(frame2)
        entry.grid(row=i, column=1, padx=15, pady=10, sticky="ew")
        entries.append(entry)

# ----------------------------------------------------------------------------------------------------------
    frame3 = tk.Frame(windowAdd, relief="raised", borderwidth=4)
    frame3.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    button = tk.Button(frame3, text="Daten Speichern", command=lambda: entryPerson(entries,typeOfPerson))
    button.pack()

    windowAdd.mainloop()

def selectRecordsGUI(typeOfPerson):
    pass

def printFullDatabaseGUI(typeOfPerson):
    pass
def changeRecordsGUI(typeOfPerson):
    pass

def printBirthdaysEmployeeGUI():
    pass

def closeDatabase():
    pass


def getMainMenuButtons(menuItems, windowMain):
    mainMenuButtons = [[menuItems[0],lambda: addNewRecordGUI(windowMain, "Employee")],
                       [menuItems[1],lambda: addNewRecordGUI("Visitor")],
                       [menuItems[2],lambda: selectRecordsGUI("Employee")],
                       [menuItems[3],lambda: printFullDatabaseGUI("Employee")],
                       [menuItems[4],lambda: selectRecordsGUI("Visitor")],
                       [menuItems[5],lambda: printFullDatabaseGUI("Employee")],
                       [menuItems[6],lambda: changeRecordsGUI("Employee")],
                       [menuItems[7],lambda: changeRecordsGUI("Visitor")],
                       [menuItems[8],lambda: printBirthdaysEmployeeGUI()],
                       [menuItems[9],lambda: closeDatabase()]]
    return mainMenuButtons


def mainmenuGUI():
    windowMain = tk.Tk()
    windowMain.title("Der Datenbank für Mitarbeiter*innen und Besucher*innen")
    windowMain.grid_columnconfigure(0, weight=1)
    windowMain.grid_rowconfigure(0, weight=1)
    windowMain.grid_rowconfigure(1, weight=1)

    firstLabelInFrame(windowMain,"Willkommen in der Datenbank!")

#-----------------frame with buttons
    frame2 = tk.Frame(windowMain, relief="raised", borderwidth=4)
    frame2.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    frame2.grid_rowconfigure(0, weight=1)
    frame2.grid_columnconfigure(0, weight=1)

    #mainMenubuttons = getMainMenuButtons(getMainMenuItems())
    mainMenubuttons = getMainMenuButtons(getMainMenuItems(), windowMain)

    for i in range(len(mainMenubuttons)):
        frame = tk.Frame(frame2)
        frame.grid(row=i, column=0, padx=50, pady=10, sticky="ew")
        button = tk.Button(frame, text=mainMenubuttons[i][0], command=mainMenubuttons[i][1])
        button.pack()

    windowMain.mainloop()

