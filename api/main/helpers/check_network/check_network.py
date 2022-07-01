from colorama import *
from api.main.constants.constants import constants
import requests

"""
This function checks the network status and Sanfoundry's webpage status, 
it returns status. 
"""
def check_network():
    try:
        data = constants["DATA"]
        request = requests.get(constants["SANFOUNDRY_WEBSITE"])
        if request.status_code != 200:
            return constants["NO_INTERNET_CONNECTION"]
        return data
    except:
            return constants["NO_INTERNET_CONNECTION"]
