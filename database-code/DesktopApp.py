# DesktopApp.py

import tkinter as tk
from tkinter import ttk
import Gui as gui
import DatabaseGraphing

class Application(ttk.Notebook):
    def __init__(self, controller, master=None):
        # Call the super constructor
        super().__init__(master)

        # Save the controller as a member variable
        self.controller = controller

        # Create the GUI
        self.master = master
        self.pack()
        self.create_widgets()

    def quit(self):
        self.master.destroy()

    def create_widgets(self):
        value = gui.SingleTab( self.controller, self )
        self.add( value, text="Value")

    def control():
        print("Hello")


if __name__ == "__main__":
    # Create a graphing controller
    graphController = DatabaseGraphing.Graphing()

    # Create a new Application Object
    mainWindow = tk.Tk()
    application = Application( graphController, mainWindow )

    # Run the application logic
    tk.mainloop()
