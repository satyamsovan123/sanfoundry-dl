from api.main.constants.constants import constants
from api.main.helpers.debugger_alert.debugger_alert import debugger_alert
import re
import time
import random

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

"""
This function is the core of this entire app. This function takes a URL as input and checks it.
It uses required libraries to scrap the questions and answers therefore, it uses JavaScript codes that runs in the browser (automatically) to get the required DOM elements.
"""
def get_questions_answers(url):
    contents = []
    data = constants["DATA"]
    if(url == ""):
        data = constants["INVALID_URL"]
        debugger_alert(data, "Error")
        return (data, contents)
    try:
        time.sleep(random.randint(4, 9))
        user_agent = constants["user_agent_list"][random.randint(0, len(constants["user_agent_list"]) - 1)]
        # print(user_agent)
        options = Options()
        options.headless = True
        options.add_argument("--window-size = 1920, 1080")
        options.add_argument("--no-sandbox")
        options.add_argument(f'user-agent={user_agent}')
        # chrome_driver_location = Service(r"api/main/helpers/drivers/chromedriver")
        # browser = webdriver.Chrome(options = options, service = chrome_driver_location)
        browser = webdriver.Chrome(options = options, service = ChromeDriverManager().install())
        time.sleep(3)
        browser.get(url)

        print("____EXECUTING JS____")
        all_raw_questions = browser.execute_script('''
            all_questions = []
            all_p_tags = document.querySelectorAll(".entry-content p")
            all_p_tags.forEach(p_tag => {
                previous_child = p_tag.previousSibling.previousSibling
                if(previous_child) {
                    if(previous_child.className == "hk1_style-wrap5") {
                        code = ""
                        code = previous_child.innerText
                        // console.log("---------code----------")
                        // console.log(code)
                        all_questions.push(code)
                    }
                }
                if((p_tag.outerHTML).includes("href")) {
                    // console.log("---------images----------")
                    // console.log(p_tag.outerHTML)
                    all_questions.push(p_tag.outerHTML)
                } else {
                    // console.log("---------normal question----------")
                    // console.log(p_tag.innerText)
                    all_questions.push(p_tag.innerText)
                }
            })
            return all_questions
        ''')
        print("____CHECKING ALL QUESTIONS____")

        all_raw_questions.pop(0)
        last_substring = "Sanfoundry Global Education & Learning Series"
        last_substring_element = [question for question in all_raw_questions if last_substring in question]
        last_substring_index = all_raw_questions.index(last_substring_element[0])
        all_raw_questions = all_raw_questions[:last_substring_index]
        all_raw_questions = [question.replace("View Answer", "") for question in all_raw_questions if (len(question) != 0)]
        all_questions = []
        for question in all_raw_questions:
            is_html = bool(BeautifulSoup(question, "html.parser").find())
            if(is_html):
                question_with_image = ""
                question_soup = BeautifulSoup(question, features = "html.parser")
                temp_p = question_soup.find("p")
                temp_a = question_soup.find("a")
                if(temp_p):
                    question_with_image = question_with_image + temp_p.get_text()
                if(temp_a):
                    url_regex = r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#\?&\/\/=]*)"
                    all_links_in_question = re.findall(url_regex, str(temp_a))
                    all_links_in_question = [constants["SANFOUNDRY_WEBSITE"] + link + "\n" for link in all_links_in_question]
                    all_links_in_question = [link for link in all_links_in_question if ("png" or "jpg" or "jpeg") in link]
                    all_links_in_question = list(set(all_links_in_question))
                    all_links_in_question = ' '.join(link for link in all_links_in_question)

                    question_with_image = question_with_image + all_links_in_question
                else:
                    all_questions.append("\n" + question + "\n")

                if(question_with_image):
                    all_questions.append("\n" + question_with_image + "\n")
            else:
                all_questions.append(question)
        print("____GOT ALL QUESTIONS____")

        all_answers = []
        print("____EXECUTING JS____")
        all_raw_answers = browser.execute_script('''
            all_answers = []
            all_div_tags = document.querySelectorAll(".collapseomatic_content ")
            all_div_tags.forEach(answer => all_answers.push(answer.innerText))
            return all_answers
        ''')
        all_raw_answers = [answer for answer in all_raw_answers if (answer.startswith('Answer') or answer.startswith(' Answer'))] 
        all_raw_answers = [answer.strip('\n').strip('\t').replace("\n", " ") for answer in all_raw_answers]
        print("____CHECKING ALL ANSWERS____")
        for answer in all_raw_answers:
            total_answer = answer.split("Explanation")
            answer = total_answer[0][:-1]
            explanation = "Explanation" + total_answer[1]
            all_answers.append({"answer": answer, "explanation": explanation})
        print("____GOT ALL ANSWERS____")
        
        contents = [all_questions, all_answers]
        print(contents)
        return (data, contents)

    except:
        data = constants["UNABLE_TO_SCRAP_PAGE"]
        debugger_alert(data, "Error")
        return (data, contents)

