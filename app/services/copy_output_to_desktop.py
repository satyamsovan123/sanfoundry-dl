import shutil
import os
from .logger import logger

""" 
This function copies the final output image to the desktop.
"""
def copy_final_output_to_desktop(path_to_image):
    destination_path = ""
    # Path to the desktop folder
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

    # Ensure the desktop path exists
    if not os.path.exists(desktop_path):
        os.makedirs(desktop_path)

    # Destination path on the desktop
    destination_path = os.path.join(desktop_path, 'final_image_output.jpeg')

    try:
        # Copy the generated image to the desktop
        shutil.copy(path_to_image, destination_path)
        return destination_path  
    except Exception as exception:
        logger(f"An error occured while copying the final output to the desktop - {exception}")
        return ""