from flask import *
from api.main.constants.constants import constants

from api.main.helpers.debugger_alert.debugger_alert import debugger_alert
from api.main.controller.scrap.scrap import scrap as main_scrap
from api.main.helpers.check_network.check_network import check_network

url_list = [
    "https://www.sanfoundry.com/operating-system-questions-answers/",
    "https://www.sanfoundry.com/computer-network-questions-answers/",
    "https://www.sanfoundry.com/software-engineering-questions-answers/",
    "https://www.sanfoundry.com/software-architecture-design-questions-answers/",

    "https://www.sanfoundry.com/1000-data-structure-questions-answers/",
    "https://www.sanfoundry.com/1000-data-structures-algorithms-ii-questions-answers/",
    "https://www.sanfoundry.com/1000-computer-organization-architecture-questions-answers/",
    "https://www.sanfoundry.com/1000-database-management-system-questions-answers/",
    "https://www.sanfoundry.com/1000-compilers-questions-answers/",
    "https://www.sanfoundry.com/1000-automata-theory-questions-answers/",
    "https://www.sanfoundry.com/1000-computer-fundamentals-questions-answers/",
    "https://www.sanfoundry.com/1000-cryptography-network-security-questions-answers/",
    "https://www.sanfoundry.com/1000-cyber-security-questions-answers/",
    "https://www.sanfoundry.com/1000-cloud-computing-questions-answers/",
    "https://www.sanfoundry.com/1000-computer-graphics-questions-answers/"
]

app = Flask(__name__, static_folder = constants["FOLDER_NAME"])

"""
This route serves for checking the app status
"""
@app.route('/', methods = ["GET"])
def index():
    data = "sanfoundry-dl is running"
    status = 200
    debugger_alert(data, "Success")
    return jsonify({"message": data}), status

"""
This route handles the downloading result.pdf file
"""
@app.route('/download_pdf', methods=['GET'])
def download_pdf():    
    return send_from_directory(constants["FOLDER_NAME"], constants["RESULT_FILE_NAME"] + ".pdf")

"""
This route handles the POST and GET for the main scrap route
"""
@app.route('/scrap', methods=['GET', 'POST'])
def scrap():
    data = check_network()
    if(data == constants["NO_INTERNET_CONNECTION"]):
        # return jsonify({"message": data})
        return render_template('error.html', data = data)

    if (request.method) == 'GET':
        return render_template('index.html')
    elif (request.method) == 'POST':
        if(request.form['url']):
            url = request.form['url']
            data, contents = main_scrap(url)
            # print(data, contents)
            if(len(contents) != 0 or data == constants["DATA"]):
                return render_template('download.html')
            else:
                return render_template('error.html', data = data)
        else:
            data = constants["INVALID_URL"]
            contents = []
        # return jsonify({"data": data, "contents": contents})
    else:
        return render_template('error.html')

"""
This route handles the error and the invalid routes
"""
@app.errorhandler(404)
def error(error):
    # debugger_alert(error)
    return render_template('error.html')

"""
This function serves as the main entry point for the entire app.
"""
if __name__ == "__main__":
    app.run(debug = True)