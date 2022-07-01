import os
import shutil
import re
import time
import glob
from fpdf import FPDF
pdf = FPDF()

from api.main.service.sanitize_list.sanitize_list import sanitize_list
from api.main.service.scrappers.get_questions_answers.get_questions_answers import get_questions_answers
from api.main.service.scrappers.get_sub_links.get_sub_links import get_sub_links
from api.main.service.write_to_txt.write_to_txt import write_to_txt
from api.main.constants.constants import constants
from api.main.helpers.debugger_alert.debugger_alert import debugger_alert
from api.main.helpers.check_url_type.check_url_type import check_url_type

"""
This function is the main function, which combines all the modules together, 
the argument to the function is a URL, it checks the URL and calls the other dependent modules to get data.
This function also deletes all the temporary .txt files generated and creates a single .pdf file in the output folder.
"""
def scrap(url):
    contents = []
    not_scrapped_urls = []
    print("____INSIDE MAIN ENDPOINT____")

    start_time = time.time()
    
    data = constants["INVALID_URL"]
    url_regex = r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#\?&\/\/=]*)"
    is_url = re.search(url_regex , url)
    if(is_url == None):
        debugger_alert(data, "Error")
        return data, contents

    if("sanfoundry" not in url):
        debugger_alert(data, "Error")
        return data, contents

    url_type = check_url_type(url)

    print("____CORRECT URL____")
    try:
        current_folders = os.listdir(os.getcwd())
        if(constants["FOLDER_NAME"] in current_folders):
            shutil.rmtree(constants["FOLDER_NAME"])
            os.mkdir(constants["FOLDER_NAME"])
        else:
            os.mkdir(constants["FOLDER_NAME"])
    except:
        data = constants["UNABLE_TO_READ_TO_FILE"]
        return data, contents
    print("____CHECKED OUTPUT FOLDER____")

    if(url_type == constants["TYPE_B_URL"]): 
        data, contents = get_questions_answers(url)
        if(len(contents) == 0):
            data = constants["UNABLE_TO_SCRAP_PAGE"]
            return data, contents

        message, all_items = sanitize_list(contents[0], contents[1])
        data_mismatch = False
        if(message == constants["DATA_MISMATCH_WARNING"]):
            data_mismatch = True
        write_to_txt(all_items, data_mismatch, url)

        # debugger_alert(data, "Success")
        # return data, contents
        total_contents = all_items
    
    elif(url_type == constants["TYPE_A_URL"]):
        total_contents = []  
        data, all_sub_links = get_sub_links(url)
        if(len(all_sub_links) == 0):
            return data, contents
        index = 1
        for url in all_sub_links:
            print(str(index) + " of " + str(len(all_sub_links)))
            data, contents = get_questions_answers(url)
            # total_contents.append(contents)
            index += 1
            if(len(contents) == 0):
                data = str(index) + " " + constants["UNABLE_TO_SCRAP_PAGE"] + " : " + url
                not_scrapped_urls.append(url)
                debugger_alert(data, "Error")
                continue
                # return data, contents

            message, all_items = sanitize_list(contents[0], contents[1])
            # print(all_items)
            data_mismatch = False
            if(message == constants["DATA_MISMATCH_WARNING"]):
                data_mismatch = True
            write_to_txt(all_items, data_mismatch, url)
        
    try:
        print("____MAKING ALL TEXT AS ONE FILE____")
        os.chdir(constants["FOLDER_NAME"])
        all_text_files = glob.glob("*.txt")
        with open(constants["RESULT_FILE_NAME"] + ".txt", "wb") as outfile:
            for text_file in all_text_files:
                with open(text_file, "rb") as infile:
                    outfile.write(infile.read())
                os.remove(text_file)
    except:
        data = constants["UNABLE_TO_DELETE_RESIDUE_FILE"]
        debugger_alert(data, "Warning") 
        
    try:
        print("____MAKING PDF FILE____")
        pdf.add_page()
        pdf.set_font("Arial", size = 12)
        text_file = open(constants["RESULT_FILE_NAME"] + ".txt", "r")
        for line in text_file:
            pdf.multi_cell(180, 10, txt = line.encode('latin-1', 'replace').decode('latin-1'))
        pdf.output(constants["RESULT_FILE_NAME"] + ".pdf")  
        os.remove(constants["RESULT_FILE_NAME"] + ".txt")
    except:
        data = constants["UNABLE_TO_CREATE_PDF"]
        debugger_alert(data, "Warning") 
        
    print("____ENDING____")
        
    time_taken = "Process took %s seconds" % (time.time() - start_time)
    debugger_alert(time_taken, "SUCCESS") 

    contents = total_contents
    return data, contents
 