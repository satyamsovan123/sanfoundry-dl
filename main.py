from flask import Flask
from flask import *
from api.main.constants.constants import constants

from api.main.helpers.debugger_alert.debugger_alert import debugger_alert
from api.main.controller.scrap.scrap import scrap as main_scrap
from api.main.helpers.check_network.check_network import check_network

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
        return render_template('error.html', data = data)
    if (request.method) == 'GET':
        return render_template('index.html')
    elif (request.method) == 'POST':
        if(request.form['url']):
            url = request.form['url']
            data, contents = main_scrap(url)
            if(len(contents) != 0 or data == constants["DATA"]):
                return render_template('download.html')
            else:
                return render_template('error.html', data = data)
        else:
            data = constants["INVALID_URL"]
            contents = []
    else:
        return render_template('error.html')

"""
This route handles the POST and GET for the main scrap route, this returns JSON instead of webpages
"""
@app.route(constants["API_VERSION"] + 'scrap', methods=['POST'])
def api_scrap():
    data = check_network()
    if(data == constants["NO_INTERNET_CONNECTION"]):
        return jsonify({"data": data})

    try:
        if(request.form['url']):
            url = request.form['url']
            data, contents = main_scrap(url)
            if(len(contents) != 0 or data == constants["DATA"]):
                return jsonify({"data": data, "contents": contents})
            else:
                data = constants["UNABLE_TO_SCRAP"]
                return jsonify({"data": data, "contents": contents})
        else:
            data = constants["INVALID_URL"]
            contents = []
            return jsonify({"data": data, "contents": contents})
    except:
        data = constants["UNABLE_TO_SCRAP"]
        contents = []
        return jsonify({"data": data, "contents": contents})

"""
This route handles the error and the invalid routes
"""
@app.errorhandler(404)
def error(error):
    return render_template('error.html')

"""
This function serves as the main entry point for the entire app.
"""
if __name__ == "__main__": 
    app.run(debug = True)