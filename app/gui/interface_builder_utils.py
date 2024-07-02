
import tkinter as tk
import os
from ..services.logger import logger
from ..constants import constants

""" 
This function centers the window on the screen.
It returns the dimensions of the window in the format "widthxheight+x+y".
"""
def center_window_on_screen(element):
    try:
        x = (element.winfo_screenwidth() // 2) - (element.winfo_width() // 2)
        y = (element.winfo_screenheight() // 2) - (element.winfo_height() // 2)
        return f"{element.winfo_width()}x{element.winfo_height()}+{x}+{y}"

    except Exception as exception:
        logger(f"An error occured while centering the window on the screen - {exception}")
        return constants["DEFAULT_DIMENSIONS"]


""" 
This function shows a custom messagebox.
It takes the app, title and message as input.

"""
def show_custom_messagebox(app, title, message):
    try:
        # New Window
        custom_messagebox_window = tk.Toplevel(app)
        custom_messagebox_window.title(title)
        custom_messagebox_window.resizable(False, False)

        # Message Label
        message_label = tk.Label(custom_messagebox_window, text = message, padx = 50, pady = 50)
        message_label.pack()
        
        # Okay Button
        ok_button = tk.Button(custom_messagebox_window, text = "Okay", command = custom_messagebox_window.destroy)
        ok_button.pack(padx = 20, pady = 20)
        
        # Center Window
        custom_messagebox_window.update_idletasks()
        dimensions = center_window_on_screen(custom_messagebox_window)
        custom_messagebox_geometry = dimensions
        custom_messagebox_window.geometry(custom_messagebox_geometry)

        custom_messagebox_window.transient(app)
        custom_messagebox_window.grab_set()
        app.wait_window(custom_messagebox_window)
    
    except Exception as exception:
        logger(f"An error occured while showing the custom messagebox - {exception}")


