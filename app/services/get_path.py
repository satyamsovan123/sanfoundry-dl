import os
import sys

""" 
This function returns the path to the icon file.
It helps to set path for accessing files locally and in the executable file.
"""
def get_icon_path():
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, "assets") # Executable path
    else:
        return os.path.join(os.path.dirname(__file__), "../../assets/") # Development path

""" 
This function returns the path to output folder.
It helps to set path for accessing files locally and in the executable file.
"""
def get_output_path():
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, "sanfoundry-dl-output") # Executable path
    else:
        return os.path.join("sanfoundry-dl-output") # Development path
    
""" 
This function returns the path to where log file is stored.
It helps to set path for accessing files locally and in the executable file.
"""
def get_log_path():
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, "sanfoundry-dl.log") # Executable path
    else:
        return os.path.join("sanfoundry-dl.log") # Development path