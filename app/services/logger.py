import datetime
import os
LOG_FILE = "log.log"

""" 
This clears the log file before starting the application.
"""
if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

""" 
This function logs the message to the console and writes it to the log file.
"""
def logger(message):
    print(f"{message}")
    write_to_log(f"{datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")} - {message}")

""" 
This function writes the message to the log file.
"""
def write_to_log(message):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{message}\n")

