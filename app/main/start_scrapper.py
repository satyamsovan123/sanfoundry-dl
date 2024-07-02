from ..constants import constants
from datetime import datetime
from .create_folders import create_folders
from .get_data_from_website import get_all_questions_and_answers_from_website
from .generate_output import generate_image_output
from ..services.logger import logger
import os
import re
from ..services.get_path import get_output_path
path = get_output_path()
from ..services.copy_output_to_desktop import copy_final_output_to_desktop
from ..services.clean_up import clean_up

""" 
This function starts the scrapper by checking the URL and calling the necessary functions.
"""
def start_scrapper(url):
    # Check if the URL is valid
    if not re.match(r"(https?://)?(www\.)?sanfoundry\.com(/.*|#.*)?", url):
        logger(f"Invalid URL")
        return constants["INVALID_URL"]
    
    logger(f"Starting the scrapping for the URL - {url}")
    
    # https://www.sanfoundry.com/quantitative-aptitude-questions-answers/
    # Check if the website has only questions and answers
        # Then scrap_for_questions_and_answers()

    # https://www.sanfoundry.com/1000-network-theory-questions-answers/
    # Check if the website has just the tables with different topics
        # Then scrap_tables_for_links() and loop through each table
            # Then scrap_for_questions_and_answers()

    # https://www.sanfoundry.com/1000-python-questions-answers/
    # Check if the website has both questions and answers and tables
        # Then scrap_for_questions_and_answers()
        # Then scrap_tables_for_links() and loop through each table
            # Then scrap_questions_and_answers()

    # Create "sanfoundry-dl-output" directory
    create_folders()
    start_time = datetime.now() 

    # Get all the questions and answers from the website
    get_all_questions_and_answers_from_website(url)

    # Generate the final image output
    generate_image_output(os.path.join(path))
    
    message = f"Successfully scrapped the website. Please check the your desktop folder for the final image."

    # Check if the final image is generated
    if not os.path.exists(os.path.join(path) + "/final_image_output.jpeg"):
        message = "An error occured while scrapping the website. Please try again."

    # Copy the final image to the desktop
    copy_final_output_to_desktop(os.path.join(path) + "/final_image_output.jpeg")

    # Clean up the "sanfoundry-dl-output" directory
    clean_up()
    end_time = datetime.now()

    logger(f"Time taken to scrap the website - {end_time - start_time}")
    return message 

