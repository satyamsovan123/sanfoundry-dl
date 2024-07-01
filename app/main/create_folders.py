import os
import shutil
from ..constants import constants

""" 
This function creates an output directory and deletes the existing one if it exists.
"""
def create_folders():
    output_dir = constants["OUTPUT_FOLDER"]
    # Create an output directory if it doesn't exist
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)  # Delete the output directory and its contents
    os.makedirs(output_dir)  # Create a new output directory
