import tkinter as tk

from EntryMenuGUI import *
from checkFunctions import *
from dataFunctions import *
from tkinter import messagebox

def firstLabelInFrame(window, text):
    frame1 = tk.Frame(window, relief = "raised", borderwidth=4)
    frame1.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    label = tk.Label(frame1, text=text, bg="light gray")
    label.pack(pady=10, expand=True)

def backToMainMenu(window):
    window.destroy()
    mainmenuGUI()
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#------------------------entry menu-------------------------------------------------


def selectRecordsGUI(windowMain, typeOfPerson):
    pass

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#------------------------print menu-------------------------------------------------
def printFullDatabaseGUI(windowMain,typeOfPerson):
    atributesList = chooseAtributesList(typeOfPerson)
    windowPrint = tk.Tk()
    windowMain.destroy()
    windowPrint.grid_columnconfigure(0, weight=1)
    windowPrint.grid_rowconfigure(0, weight=1)
    windowPrint.grid_rowconfigure(1, weight=1)
    pass



def changeRecordsGUI(typeOfPerson):
    pass

def printBirthdaysEmployeeGUI():
    pass

def closeDatabase():
    pass
#-----------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#---------------------------------------main menu------------------------------------------------
def getMainMenuButtons(menuItems, windowMain):
    mainMenuButtons = [[menuItems[0],lambda: addNewRecordGUI(windowMain, "Employee")],
                       [menuItems[1],lambda: addNewRecordGUI(windowMain,"Visitor")],
                       [menuItems[2],lambda: selectRecordsGUI(windowMain, "Employee")],
                       [menuItems[3],lambda: printFullDatabaseGUI(windowMain,"Employee")],
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
# -----------------frame with first label
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

