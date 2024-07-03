
import os
import time
import random
import re
import sys
import shutil
import base64
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
def get_all_questions_and_answers_from_website_by_taking_screenshots(website):
    logger(f"Getting all questions and answers from the website by taking screenshots")
    try:
        # Set up the Selenium browser
        logger(f"Setting up the browser")
        driver_path = ChromeDriverManager().install()
        logger(f"chrome - {shutil.which("google-chrome")}\ndriver - {driver_path}")
        chrome_options = Options()
        chrome_options.add_argument("--headless") # Run the browser in headless mode
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
        

""" 
This function gets all the questions and answers from the website.

It gets everything one by one manually in a dictionary.
"""
def get_all_questions_and_answers_from_website_by_text_v1(website):
    logger(f"Getting all questions and answers from the website by text")
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

        # Ads doesn't matter

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

        raw_question_and_answers = []
        
        logger(f"Finding ...")
        for index, paragraph_tag in enumerate(paragraph_tags):
            logger(f"Finding question {index}")
            raw_content = {}

            # Get the raw question content
            raw_content['raw_data'] = paragraph_tag.text


            # Get the question's text content
            raw_content['question'] = paragraph_tag.text


            # Extract all the links from the paragraph tag
            # These might be pictures related to the question or some other links
            try:
                links = paragraph_tag.find_elements(By.TAG_NAME, "a")
                raw_content['links'] = []
                for link in links:
                    raw_content['links'].append(link.get_attribute("href"))
            
            except Exception as exception:
                raw_content['links'] = []
                logger(f"Links not found for question {index}")
                continue


            # Find pre tag after paragraph tag (for code snippets)
            # The pre tag is always present nested inside 7 levels of div tags
            # This is pretty wierd engineering
            # Ignore the ads that might be after the paragraph tag
            try:
                # Find the div with class "hk1_style-wrap5" that follows the p tag, as the pre tag is nested inside this div
                outer_div = paragraph_tag.find_element(By.XPATH, 'following-sibling::div[contains(@class, "hk1_style-wrap5")]')
                # Find the pre tag inside the nested div structure
                pre_tag = outer_div.find_element(By.XPATH, './div/div/div/div/div/div/pre')
                raw_content['extra_content_1'] = pre_tag.text

            except Exception as exception:
                raw_content['extra_content_1'] = ""
                logger(f"Pre tag not found for question {index}")
                continue


            # Find the span tag within the p tag, whose id attribute is used to find the div tag which contains the answer and explanation
            # Basically, it's the view answer button
            try:
                span_tag = paragraph_tag.find_element(By.TAG_NAME, 'span')

                # The div tag which contains the answer and explanation has an id attribute equal to the span tag's id attribute with "target-" as a prefix
                span_answer_id = "target-" + span_tag.get_attribute('id')

                # Find the corresponding div
                script_to_get_answer_div = f"return document.getElementById('{span_answer_id}').innerHTML;"
                answer_div = browser.execute_script(script_to_get_answer_div)
                raw_content['answer'] = answer_div

            except Exception as exception:
                raw_content['answer'] = ""
                logger(f"Span tag not found for question {index}")
                continue


            # Find the pre tag following the p tag (for code snippets and tables)
            try:
                pre_tag = paragraph_tag.find_element(By.XPATH, 'following-sibling::pre')
                raw_content['extra_content_2'] = pre_tag.text

            except Exception as exception:
                raw_content['extra_content_2'] = ""
                logger(f"Pre tag not found for question {index}")
                continue

            raw_question_and_answers.append(raw_content) # Append the raw content to the list

        for element in raw_question_and_answers:
            logger(f"------------------------")
            # logger(f"Raw data - {element['raw_data']}")
            # logger("\n")
            logger(f"Question - {element['question']}")
            logger("\n")
            logger(f"Extra content 1 - {element['extra_content_1']}")
            logger("\n")
            logger(f"Extra content 2 - {element['extra_content_2']}")
            logger("\n")
            logger(f"Links - {element['links']}")
            logger("\n")
            logger(f"Answer - {element['answer']}")
            logger("\n")
            logger(f"------------------------")
            
        browser.quit() # Close the browser

    except TimeoutException:
            logger(f"The questions and answers were not found within the specified time")

    except Exception as exception:
        logger(f"An error occured while checking for the questions and answers div - {exception}")
        

""" 
This function gets all the questions and answers from the website.

It deletes the advertisements, expands all the answers, and hides the 'View Answer' buttons.
It then saves the HTML content to a file. 
This is better than the previous function as it gets all the content in one go.
"""
def get_all_questions_and_answers_from_website_by_text_v2(website):
    logger(f"Getting all questions and answers from the website by text")
    try:
        # Set up the Selenium browser
        logger(f"Setting up the browser")
        driver_path = ChromeDriverManager().install()
        logger(f"chrome - {shutil.which("google-chrome")}\ndriver - {driver_path}")
        chrome_options = Options()
        # chrome_options.add_argument("--headless") # Run the browser in headless mode
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--print-to-pdf-no-header")
        chrome_options.add_argument("--kiosk-printing")
        
        chrome_options.add_argument(f"user-agent = {__get_random_user_agent()}")  # Set a random user agent
        browser = webdriver.Chrome(service = Service(driver_path), options = chrome_options)  # Initialize the browser
        # browser = webdriver.Chrome(options = chrome_options)  # Initialize the browser (for render.com / heroku.com deployment)
        browser.get(website) # Open the website

        # Ads doesn't matter

        # Do random actions
        __make_it_humane(browser) 

        time.sleep(__get_random_medium_timeout())
        
        # Wait for 10 seconds for the entry-content div to appear
        entry_content_div = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.entry-content"))
        )

        # Execute JavaScript to remove elements with class names containing "ads" or "google"
        # Remove the ads
        logger(f"Removing ads")
        browser.execute_script("""
            const elements = document.querySelectorAll('div.entry-content *');
            elements.forEach(function(element) {
                const classList = element.className.split(' ');
                for (let i = 0; i < classList.length; i++) {
                    if (classList[i].includes('ads') || classList[i].includes('google')) {
                        element.parentNode.removeChild(element);
                        break;
                    }
                }
            });
        """)


        logger(f"Expanding all the answers")
        # Apply 'display: block' to all elements with IDs starting with 'target-'
        browser.execute_script("""
            const elements = document.querySelectorAll('[id^="target-"]');
            elements.forEach(function(element) {
                element.style.display = 'block';
            });
        """)

        # Hide the 'View Answer' buttons'
        # Hide all elements with class 'collapseomatic'
        logger(f"Hiding all view answer button")
        browser.execute_script("""
            const elements = document.querySelectorAll('.collapseomatic');
            elements.forEach(function(element) {
                element.style.opacity = '0';
            });
        """)

        # Execute JavaScript to remove all elements after the specific <strong> element
        # Remove unnecessary elements
        browser.execute_script("""
            var entryContent = document.querySelector('div.entry-content');
            var strongElements = entryContent.getElementsByTagName('strong');
            var found = false;

            for (var i = 0; i < strongElements.length; i++) {
                if (strongElements[i].textContent.trim() === "Sanfoundry Global Education & Learning Series – Data Structures & Algorithms.") {
                    found = true;
                    var sibling = strongElements[i].nextSibling;
                    while (sibling) {
                        var nextSibling = sibling.nextSibling;
                        sibling.remove();
                        sibling = nextSibling;
                    }
                    break;
                }
            }

            if (!found) {
                console.warn('Specified <strong> element not found.');
            }
        """)
       
        output_file_path = os.path.join(path, f"final_html_output.html")

        # Write the HTML content to the file, overwriting if it already exists
        with open(output_file_path, "w", encoding = "utf-8") as file:
            file.write(entry_content_div.get_attribute('innerHTML'))

 
        browser.get(f"file:///{os.path.abspath(output_file_path)}")

        # Configure print options
        print_options = {
            'landscape': False,
            'displayHeaderFooter': False,
            'printBackground': True,
            'preferCSSPageSize': True,
        }

        # Use the Chrome DevTools Protocol to print the page to PDF
        result = browser.execute_cdp_cmd("Page.printToPDF", print_options)

        # Decode the base64-encoded PDF data
        pdf_data = base64.b64decode(result['data'])

        pdf_file_path = os.path.join(path, 'final_pdf_output.pdf')

        # Save the PDF to file
        with open(pdf_file_path, "wb") as file:
            file.write(pdf_data)


        browser.quit() # Close the browser



    except TimeoutException:
        logger(f"The questions and answers were not found within the specified time")

    except Exception as exception:
        logger(f"An error occured while checking for the questions and answers div - {exception}")

        
