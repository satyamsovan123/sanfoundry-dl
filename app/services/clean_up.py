import os
import shutil
from .logger import logger
from .get_path import get_output_path
path = get_output_path()

""" 
This function cleans up the "sanfoundry-dl-output" directory.
"""
def clean_up():
    logger(f"Cleaning up the output directory")

    try:    
        # Remove the output directory and its contents
        if os.path.exists(os.path.join(path)):
            shutil.rmtree(os.path.join(path))

    except Exception as exception:
        logger(f"An error occured while cleaning up the output directory - {exception}")