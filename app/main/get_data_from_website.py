
import os
import time
import random
import re
import sys
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..services.logger import logger
from ..constants import constants
from ..services.get_path import get_output_path
path = get_output_path()
logger(f"Path - {os.path.join(path)}")

""" 
This function generates a random user agent.
"""
def __get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    ]
    return random.choice(user_agents)

""" 
This function generates a random timeout of medium duration.
"""
def __get_random_medium_timeout():
    medium_timeout = random.randint(4, 7)
    return medium_timeout
 
""" 
This function generates a random timeout of small duration.
"""
def __get_random_small_timeout():
    small_timeout = random.randint(1, 2)
    return small_timeout

""" 
This function scrolls to the bottom of the page randomly.
"""
def scroll_to_bottom(browser):
    try:
        should_scroll = random.choice([True, False]) # Randomly decide to scroll to the bottom of the page
        if(should_scroll):
            logger(f"⬇️")
            time.sleep(__get_random_small_timeout()) # Wait for few seconds
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll to the bottom of the page

    except Exception as exception:
        logger(f"An error occured while scrolling to the bottom of the page - {exception}")

""" 
This function scrolls to the top of the page randomly.
"""
def scroll_to_top(browser):
    try:
        should_scroll = random.choice([True, False])
        if(should_scroll):
            logger(f"⬆️")
            browser.execute_script("window.scrollTo(0, 0);") # Scroll to the top of the page
            time.sleep(__get_random_small_timeout()) # Wait for few seconds

    except Exception as exception:
        logger(f"An error occured while scrolling to the top of the page - {exception}")

""" 
This function maximizes the window randomly.
"""
def maximize_window(browser):
    try:
        should_maximize = random.choice([True, False])
        if(should_maximize):
            logger(f"🔍")
            browser.maximize_window() # Maximize the window
    except Exception as exception:
        logger(f"An error occured while maximizing the window - {exception}")

"""
This function makes the bot humane by scrolling to the bottom, scrolling to the top, and maximizing the window randomly.
"""
def __make_it_humane(browser):
    logger(f"Making the bot humane")
    try:
        actions = ["scroll_to_bottom", "scroll_to_top", "maximize_window"]
        random.shuffle(actions) 
        for action in actions:
            getattr(sys.modules[__name__], f"{action}")(browser)  

    except Exception as exception:
        logger(f"An error occured while making the bot humane - {exception}")

def get_all_tables_from_website(url):
    pass

def get_all_links_from_table(url):
    pass

""" 
This function gets all the questions and answers from the website.

It deletes the advertisements.
It gets all the p tags within the entry-content div. As, the p tags inside the entry-content div contains questions and answers.
It takes a screenshot of the question.
The p tag also contains a span tag which has an id attribute. This span tag has id attribute is used to find the div tag which contains the answer and explanation.
It finds the div tag with the id attribute equal to the span tag's id attribute, which contains the answer and explanation.
It takes a screenshot of the answer and explanation.
"""
def get_all_questions_and_answers_from_website(website):
    try:
        # Set up the Selenium browser
        logger(f"Setting up the browser")
        driver_path = ChromeDriverManager().install()
        logger(f"chrome - {shutil.which("google-chrome")}\ndriver - {driver_path}")
        chrome_options = Options()
        # chrome_options.add_argument("--headless") # Run the browser in headless mode
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        
        chrome_options.add_argument(f"user-agent = {__get_random_user_agent()}")  # Set a random user agent
        browser = webdriver.Chrome(service = Service(driver_path), options = chrome_options)  # Initialize the browser
        # browser = webdriver.Chrome(options = chrome_options)  # Initialize the browser (for render.com / heroku.com deployment)
        browser.get(website) # Open the website

        # Close the ad if it appears
        try:
            # Wait for the page to fully load
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            # Remove elements with class "adsbygoogle" using JavaScript
            browser.execute_script("""
                let elementsToBeRemoved = document.querySelectorAll('.adsbygoogle, .bottomStickyContainer');
                    elementsToBeRemoved.forEach(function(element) {
                        element.remove();
                    });
            """)
            logger(f"Closed advertisements")
        except Exception as exception:
            logger(f"Unable to close advertisements - ${exception}")

        # Do random actions
        __make_it_humane(browser) 

        time.sleep(__get_random_medium_timeout())
        
        # Wait for 10 seconds for the entry-content div to appear
        entry_content_div = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.entry-content"))
        )

        # Find all p tags within the entry-content div
        # The p tags contains questions
        paragraph_tags = entry_content_div.find_elements(By.TAG_NAME, "p")

        logger(f"Finding ...")
        for index, paragraph_tag in enumerate(paragraph_tags):
            logger(f"Finding question {index}")
            # Take a screenshot of the question
            # paragraph_tag.screenshot(os.path.join(constants["OUTPUT_FOLDER"], f"question_{index}.png"))
            paragraph_tag.screenshot(os.path.join(path, f"question_{index}.png"))

            try:
                logger(f"Finding answer {index}")
                # Find the span tag within the p tag
                paragraph_tag.find_elements(By.TAG_NAME, "span")[0].click()
                time.sleep(__get_random_small_timeout())

                # Find the span tag's id attribute
                span_tag_answer_element_id = paragraph_tag.find_elements(By.TAG_NAME, "span")[0].get_attribute("id")
                span_answer_id = "target-" + span_tag_answer_element_id

                # Find the div tag with the id attribute equal to the span tag's id attribute
                span_answer = browser.find_element(By.ID, span_answer_id)

                # Take a screenshot of the answer
                span_answer.screenshot(os.path.join(path, f"answer_{index}.png"))
                
            except Exception as exception:
                logger(f"No answer found - {exception}")

        browser.quit() # Close the browser

    except TimeoutException:
            logger(f"The questions and answers were not found within the specified time")

    except Exception as exception:
        logger(f"An error occured while checking for the questions and answers div - {exception}")
        

