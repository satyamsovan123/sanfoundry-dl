
import tkinter as tk
import os

def center_window_on_screen(element):
    x = (element.winfo_screenwidth() // 2) - (element.winfo_width() // 2)
    y = (element.winfo_screenheight() // 2) - (element.winfo_height() // 2)
    return f"{element.winfo_width()}x{element.winfo_height()}+{x}+{y}"

def show_custom_messagebox(app, title, message):
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
    custom_messagebox_geometry = center_window_on_screen(custom_messagebox_window)
    custom_messagebox_window.geometry(custom_messagebox_geometry)

    custom_messagebox_window.transient(app)
    custom_messagebox_window.grab_set()
    app.wait_window(custom_messagebox_window)


