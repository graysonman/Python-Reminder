import tkinter as tk
from tkinter import messagebox
import time

def display_popup():
    root = tk.Tk()
    root.withdraw()  # This hides the main window

    top = tk.Toplevel(root)
    top.withdraw()

    root.attributes('-topmost', True)

    # Show popup and check for response
    response = messagebox.askokcancel("Reminder", "Put passwords in sprint sheet and configs!")
    top.focus_force()

    top.destroy()
    root.destroy()  # Clean up the root window after closing the messagebox
    
    # If the user clicked the 'X' button, response will be False
    return response

while True:
   
    if not display_popup():
        break  # Exit the loop (and the program) if the user clicked the 'X' button
    time.sleep(60)  # Wait for 3600 seconds (1 hour)
