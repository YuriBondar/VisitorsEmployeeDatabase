
from entryMenu import *
from changeAndUpdateMenu import *
from selectMenu import *
from printFullDatabaseMenu import *

def printBirthdaysEmployeeGUI():
    pass

def closeDatabase():
    pass
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# -------------------MAIN MENU-----------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
def getMainMenuButtons(menuItems, windowMain):
    mainMenuButtons = [[menuItems[0], lambda: entryMenu(windowMain, "Employee")],
                       [menuItems[1], lambda: entryMenu(windowMain, "Visitor")],
                       [menuItems[2], lambda: selectMenu(windowMain, "Employee")],
                       [menuItems[3], lambda: printFullDatabaseMenu(windowMain, "Employee")],
                       [menuItems[4], lambda: selectMenu(windowMain, "Visitor")],
                       [menuItems[5], lambda: printFullDatabaseMenu(windowMain,"Visitor")],
                       [menuItems[6], lambda: changeMenuGUI(windowMain,"Employee")],
                       [menuItems[7], lambda: changeMenuGUI(windowMain, "Visitor")],
                       [menuItems[8], lambda: printBirthdaysEmployeeGUI()],
                       [menuItems[9], lambda: closeDatabase()]]
    return mainMenuButtons


def mainMenu():
    windowMain = tk.Tk()
    windowMain.title("Der Datenbank für Mitarbeiter*innen und Besucher*innen")
    startConfigure(windowMain)
# ---------------------------------------------------------------------------------------------------------
# ---------------- INFO FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    infoFrame(windowMain,"Willkommen in der Datenbank!")

# ---------------------------------------------------------------------------------------------------------
# ---------------- BUTTONS FRAME------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
    frameButtons = tk.Frame(windowMain, relief="raised", borderwidth=4)
    frameButtons.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    startConfigure(frameButtons)

    mainMenubuttons = getMainMenuButtons(getMainMenuItems(), windowMain)

    for i in range(len(mainMenubuttons)):
        frame = tk.Frame(frameButtons)
        frame.grid(row=i, column=0, padx=50, pady=10, sticky="ew")
        button = tk.Button(frame, text=mainMenubuttons[i][0], command=mainMenubuttons[i][1])
        button.pack()

    windowMain.mainloop()

