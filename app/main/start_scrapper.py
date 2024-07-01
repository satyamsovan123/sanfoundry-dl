from ..constants import constants
from datetime import datetime
from .create_folders import create_folders
from .get_data_from_website import get_all_questions_and_answers_from_website
from .generate_output import generate_image_output
from ..services.logger import logger
import os

""" 
This function starts the scrapper by checking the URL and calling the necessary functions.
"""
def start_scrapper(url):
    if url == "":
        return constants["INVALID_URL"]
    
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

    create_folders()
    start_time = datetime.now() 
    get_all_questions_and_answers_from_website(url)
    generate_image_output(constants["OUTPUT_FOLDER"])
    end_time = datetime.now()

    message = "Successfully scrapped the website. Check the output folder for the final image."

    # Check if the final image is generated
    if not os.path.exists(constants["OUTPUT_FOLDER"] + "/final_image_output.jpeg"):
        message = "An error occured while scrapping the website. Please try again."

    logger(f"Time taken to scrap the website - {end_time - start_time}")
    return message 

