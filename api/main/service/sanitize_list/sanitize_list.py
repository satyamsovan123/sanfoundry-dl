from api.main.constants.constants import constants
from api.main.helpers.debugger_alert.debugger_alert import debugger_alert

import re

"""
This function takes the raw question and answers scrapped from the URL and cleans them, 
the arguments to the function are allthe list of questions and list of answers
This function handles the case where the length of list of question doesn't matches the length of list of answers.
"""
def sanitize_list(questions, answers):
    initial_element_pattern = r"^\s*?([0-9]+)\.[\s]"
    final_questions = []
    temp_question = ""
    total_result = []
    message = constants["DATA"]
    if(len(questions) == 0 or len(answers) == 0):
        data = constants["INVALID_CONTENTS"]
        debugger_alert(data, "Error")
        return message, total_result
    print("____SANITIZING QUESTIONS AND ANSWERS____")
    for index, element in enumerate(questions):
        current_element = questions[index].lstrip()
        if((index + 1) < len(questions)):
            next_element = questions[index + 1].lstrip()
        else:
            next_element = current_element

        current_element_match = re.match(initial_element_pattern, current_element)
        next_element_match = re.match(initial_element_pattern, next_element)

        if(current_element_match != None and next_element_match != None):
            final_questions.append(element)
        elif(current_element_match == None and next_element_match != None):
            temp_question += element
            final_questions.append(temp_question)
            temp_question = ""
        else:
            temp_question += element
            if(index == len(questions) - 1):
                final_questions.append(temp_question)

    if(len(final_questions) != len(answers)):
        message = constants["DATA_MISMATCH_WARNING"]
        debugger_alert(constants["DATA_MISMATCH_WARNING"], "Warning")

    if(message != constants["DATA_MISMATCH_WARNING"]):
        final_index = min(len(final_questions), len(answers))
        for i in range(final_index):
            total_result.append({"question": final_questions[i], "answer": answers[i]['answer'], "explanation": answers[i]['explanation']})
    else:
        total_result.append({"question": final_questions, "answer": answers})

    return message, total_result
  