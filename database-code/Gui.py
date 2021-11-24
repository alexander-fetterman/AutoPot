# gui.py
import tkinter as tk
from tkinter import ttk

class SingleTab(tk.Frame):
    def __init__(self, controller, master=None):
        # Call the super constructor
        super().__init__(master)

        # Store the controller as a member variable
        self.controller = controller

        # Create the GUI
        self.master = master
        self.pack()
        self.create_widgets()

    def quit(self):
        self.master.quit()

    def action(self):
        maxTuples = self.maxTupleFrame.inputBox.get()
        self.controller.handle( maxTuples )
        

    def create_widgets(self):
        # Create a frame to hold the user input
        self.maxTupleFrame = UserInputFrame( "Number of tuples", self )
        self.maxTupleFrame.pack(side="top")

        # Create a frame to contain the two buttons
        self.buttonFrame = ButtonContainer(self)
        self.buttonFrame.pack(side="bottom")

class UserInputFrame(tk.Frame):
    def __init__ (self, label, master=None ):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets( label )

    def quit(self):
        self.master.quit()

    def action(self):
        self.master.action()

    def create_widgets( self, label ):
        # Create a frame to contain the textBox and label
        self.inputBox = LabelBox( label, self )
        self.inputBox.pack(side="top")


class LabelBox(tk.Frame):
    def __init__(self, labelText, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.labelText = labelText
        self.create_widgets()

    def get(self):
        return self.textBox.get()

    def create_widgets(self):
        # Create a label for the user's query
        self.nthTermLabel = tk.Label(self, text=self.labelText)
        self.nthTermLabel.pack(side="left")

        # Create a text box for the user's query
        self.textBox = tk.Entry(self)
        self.textBox.pack(side="right")

class ButtonContainer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def quit(self):
        self.master.quit()

    def action(self):
        self.master.action()

    def create_widgets(self):
        # Create a button which will submit the user's query
        self.graphButton = tk.Button(self, text="GRAPH", fg="green", command=self.action)
        self.graphButton.pack(side="left")

        # Create a button to close the application
        self.quitButton = tk.Button(self, text="QUIT", fg="red",
                              command=self.quit)
        self.quitButton.pack(side="right")