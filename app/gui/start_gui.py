import tkinter as tk
import sys
import os 
from .interface_builder_utils import center_window_on_screen, show_custom_messagebox
from ..main import start_scrapper
from ..services.logger import logger
from ..services.get_path import get_icon_path

main_window = None

# Get the path (development or executable)
path = get_icon_path() 

"""
This function is called when the user clicks on the submit button.
It takes the user input (URL) as an argument and starts the scrapper.
It passes the result to the custom messagebox.
"""
def on_submit(user_input):
    logger(f"Clicked on submit button")
    result = start_scrapper(user_input.get())
    show_custom_messagebox(main_window, "sanfoundry-dl", result)

""" 
This function creates the main window of the application.
It contains a greeting label, a textbox input and a submit button.
"""
def create_main_window():
    try:
        logger(f"Creating main window")
        global main_window
        main_window = tk.Tk()
        main_window.title("sanfoundry-dl")
        main_window.resizable(False, False)

        main_window.grid_rowconfigure(0, weight = 1)
        main_window.grid_rowconfigure(1, weight = 1)
        main_window.grid_rowconfigure(2, weight = 1)
        main_window.grid_columnconfigure(0, weight = 1)

        platform = sys.platform

        # Windows and Linux
        if platform == "win32" or platform == "linux":
            logger(f"Windows or Linux detected")
            icon_path = path + "/icon.png"
            main_window.iconphoto(True, tk.PhotoImage(file = icon_path))

        # macOS
        elif platform == "darwin":
            logger(f"macOS detected")
            icon_path = path + "/icon.icns"
            main_window.iconbitmap(icon_path)
            main_window.option_add("*tearOff", False)
            menubar = tk.Menu(main_window)
            main_window.config(menu = menubar)

        # All other platforms
        if platform != "darwin":
            main_window.option_add("*tearOff", False)
            menubar = tk.Menu(main_window)
            main_window.config(menu = menubar)

        # Greeting label
        greetings_label = tk.Label(main_window, text = "Thanks for using sanfoundry-dl! Please enter the URL below.")
        greetings_label.pack(pady = 20, padx = 20)

        # Textbox input
        textbox_input = tk.Entry(main_window, width = 100) 
        textbox_input.pack(padx = 20, pady = 20)

        # Submit button
        submit_button = tk.Button(main_window, text = "Submit", command = lambda: on_submit(textbox_input))
        submit_button.pack(padx = 20, pady = 20)

        # Center window
        main_window.update_idletasks()
        main_window_geometry = center_window_on_screen(main_window)
        main_window.geometry(main_window_geometry)
    
    except Exception as exception:
        logger(f"An error occured while creating the main window - {exception}")

"""
This function starts the GUI.
"""
def start_gui():
    create_main_window()
    main_window.mainloop()