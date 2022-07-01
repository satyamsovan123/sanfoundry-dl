from colorama import *
from api.main.constants.constants import constants


"""
This function checks the type of URL user provided, 
the argument to the function is a url and it returns the type of URL. 
This app as of now only supports two type of Sanfoudry's URL i.e 
one with "1000" in the URL and other is with not "1000" in the URL.
"""
def check_url_type(url):
    if(url == ""):
        return constants["INVALID_URL"]
    elif("1000" in url):
        return constants["TYPE_A_URL"]
    else:
        return constants["TYPE_B_URL"]