from api.main.constants.constants import constants
import uuid

"""
This function writes a given URL's scrapped data to a temporary text file, 
the arguments to the function are all questions and answers list, data mismatch veriable and the URL.
If the length of list of question doesn't matches the length of list of answers, the questions and answers are written separately with a warning.
"""
def write_to_txt(all_items, data_mismatch, url):
    data = constants["UNABLE_TO_WRITE_TO_FILE"]
    if(len(all_items) == 0):
        return data
    try:
        file_name = ""
        file_name = url.split("com/")
        if(file_name):
            file_name = constants["FOLDER_NAME"] + "/" + url.split("com/")[1].replace("/", "") + ".txt"
        else:
            file_name = constants["FOLDER_NAME"] + "/" + str(uuid.uuid4()) + ".txt"
        print("____WRITING A PAGE TO A TEXT FILE____")

        if(data_mismatch == False):
            with open(file_name, "w") as file:
                    file.write("\n")
                    file.write(constants["DEBUGGER_LINE"])
                    file.write("\n")
                    file.write(url)
                    file.write(constants["DEBUGGER_LINE"])
                    file.write("\n")
            for item in all_items:
                with open(file_name, "a") as file:
                    file.write("\n")
                    file.write(item["question"])
                    file.write("\n")
                    file.write(item["answer"])
                    file.write("\n")
                    file.write(item["explanation"])
                    file.write("\n")
            
        else:
            with open(file_name, "w") as file:
                file.write("\n")
                file.write(constants["DEBUGGER_LINE"])
                file.write("\n")
                file.write(url)
                file.write(constants["DEBUGGER_LINE"])
                file.write("\n")
                file.write(constants["WARNING_LINE"])
                file.write("\n")
                file.write(constants["DATA_MISMATCH_WARNING"])
                file.write("\n")

            for question in all_items[0]["question"]:
                with open(file_name, "a") as file:
                    file.write(question)
                    file.write("\n")

            with open(file_name, "a") as file:
                file.write("\n")
                file.write("\n")
                file.write("\n")
                file.write(constants["WARNING_LINE"])
                file.write("\n")
                file.write(constants["DATA_MISMATCH_WARNING"])
                file.write("\n")
                file.write("\n")
                file.write("\n")

            for index, question in enumerate(all_items[0]["answer"]):
                with open(file_name, "a") as file:
                    file.write(str(index + 1) + " : " + question["answer"])
                    file.write("\n")
                    file.write(question["explanation"])
                    file.write("\n")

            with open(file_name, "a") as file:
                    file.write("\n")
                    file.write("\n")
                    file.write("\n")
                    file.write(constants["WARNING_LINE"])
                    file.write("\n")
                    file.write(constants["DATA_MISMATCH_WARNING"])
                    file.write("\n")

    except:
        return data