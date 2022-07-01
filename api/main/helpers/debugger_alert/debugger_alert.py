from colorama import *
from api.main.constants.constants import constants

"""
This function prints if any message needs to be printed in the console/terminal/command prompt, 
the arguments to the function are a message and type of message. 
"""
def debugger_alert(message, type):
    color = ""
    if(type == "Warning"):
        color = Fore.YELLOW
    elif(type == "Success"):
        color = Style.DIM + Fore.GREEN
    elif(type == "Error"):
        color = Fore.RED
        
    if(message):
        print(color + constants["DEBUGGER_LINE"])
        print(color + message)
        print(color + constants["DEBUGGER_LINE"])
        print(Style.RESET_ALL)
