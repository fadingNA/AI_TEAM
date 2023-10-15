'''
This file contains the GUI implementation for the Roadside Assistance Team application.
It defines the RoadsideAssistanceGUI class which creates and manages the graphical user interface.
'''
import tkinter as tk
from assistance import RoadsideAssistance
class RoadsideAssistanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Roadside Assistance Team")
        # Create and configure GUI elements
        self.label = tk.Label(self.root, text="Enter your location:")
        self.label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.button = tk.Button(self.root, text="Request Assistance", command=self.request_assistance)
        self.button.pack()
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
        # Create instance of RoadsideAssistance class
        self.assistance = RoadsideAssistance()
    def request_assistance(self):
        location = self.entry.get()
        assistance_needed = self.assistance.get_assistance(location)
        self.result_label.config(text=assistance_needed)