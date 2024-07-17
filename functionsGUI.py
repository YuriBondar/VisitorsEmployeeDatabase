import tkinter as tk


def backToMainMenu(window):
    window.destroy()
    from mainmenuGUI import mainmenuGUI
    mainmenuGUI()

def firstLabelInFrame(window, text):
    frame1 = tk.Frame(window, relief="raised", borderwidth=4)
    frame1.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    label = tk.Label(frame1, text=text, bg="light gray")
    label.pack(pady=10, expand=True)

def startConfigure(window):
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)

