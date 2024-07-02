import os
import shutil
from ..constants import constants
from ..services.logger import logger
from ..services.get_path import get_output_path
path = get_output_path()

""" 
This function creates an output directory and deletes the existing one if it exists.
"""
def create_folders():
    try:
        output_dir = constants["OUTPUT_FOLDER"]
        # Create an output directory if it doesn't exist
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)  # Delete the output directory and its contents
        os.makedirs(output_dir)  # Create a new output directory

    except Exception as exception:
        logger(f"An error occured while creating the output directory - {exception}")
