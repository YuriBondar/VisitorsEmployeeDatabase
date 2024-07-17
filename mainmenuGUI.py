import tkinter as tk
from tkinter import messagebox
from EntryMenuGUI import *
from OutputMenuGUI import *
from checkFunctions import *
from dataFunctions import *
from functionsGUI import firstLabelInFrame
from selectMenuGUI import *


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
                       [menuItems[2],lambda: selectMenuGUI(windowMain, "Employee")],
                       [menuItems[3],lambda: printFullDatabaseGUI(windowMain,"Employee")],
                       [menuItems[4],lambda: selectMenuGUI(windowMain,"Visitor")],
                       [menuItems[5],lambda: printFullDatabaseGUI(windowMain,"Visitor")],
                       [menuItems[6],lambda: changeRecordsGUI("Employee")],
                       [menuItems[7],lambda: changeRecordsGUI("Visitor")],
                       [menuItems[8],lambda: printBirthdaysEmployeeGUI()],
                       [menuItems[9],lambda: closeDatabase()]]
    return mainMenuButtons


def mainmenuGUI():
    windowMain = tk.Tk()
    windowMain.title("Der Datenbank für Mitarbeiter*innen und Besucher*innen")
    startConfigure(windowMain)
# -----------------frame with first label
    firstLabelInFrame(windowMain,"Willkommen in der Datenbank!")

#-----------------frame with buttons
    frame2 = tk.Frame(windowMain, relief="raised", borderwidth=4)
    frame2.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    startConfigure(frame2)

    mainMenubuttons = getMainMenuButtons(getMainMenuItems(), windowMain)

    for i in range(len(mainMenubuttons)):
        frame = tk.Frame(frame2)
        frame.grid(row=i, column=0, padx=50, pady=10, sticky="ew")
        button = tk.Button(frame, text=mainMenubuttons[i][0], command=mainMenubuttons[i][1])
        button.pack()

    windowMain.mainloop()

