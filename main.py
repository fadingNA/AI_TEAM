'''
This is the main file of the Roadside Assistance Team application.
It contains the main function that initializes the GUI and starts the application.
'''
import tkinter as tk
from gui import RoadsideAssistanceGUI
def main():
    root = tk.Tk()
    app = RoadsideAssistanceGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()