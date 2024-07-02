import datetime
import os
from .get_path import get_log_path
path =  os.path.join(get_log_path())
LOG_FILE = "sanfoundry-dl.log"

""" 
This clears the log file before starting the application.
"""
if os.path.exists(path):
        os.remove(path)

""" 
This function logs the message to the console and writes it to the log file.
"""
def logger(message):
    print(f"{message}")
    write_to_log_file(f"{datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")} - {message}")

""" 
This function writes the message to the log file.
"""
def write_to_log_file(message):
    try:
        with open(path, "a") as log_file:
            log_file.write(f"{message}\n")
    except Exception as exception:
        logger(f"An error occured while writing to the log file - {exception}")

