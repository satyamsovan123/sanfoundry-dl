from api.main.constants.constants import constants
from api.main.helpers.debugger_alert.debugger_alert import debugger_alert
from api.main.helpers.check_url_type.check_url_type import check_url_type
import itertools
import random
import requests
from bs4 import BeautifulSoup

"""
This function takes the URL as argument and gets the sub links for the URL.
"""
def get_sub_links(url):
    url_type = check_url_type(url)
    all_sub_links = []
    if(url_type != constants["TYPE_A_URL"]):
        data = constants["INVALID_URL"]
        debugger_alert(data, "Error")
        return (data, all_sub_links)
    data = constants["DATA"]
    try:
        session = requests.session()
        session.headers.update({'User-Agent': constants["user_agent_list"][random.randint(0, len(constants["user_agent_list"]))]})
        info = session.get(url)
        soup = BeautifulSoup(info.content, "html.parser")
        
        all_tables = []
        all_tables = soup.find_all("table")
        if(all_tables == []):
            data = constants["UNABLE_TO_FIND_ELEMENT"] + ": table"
            debugger_alert(data, "Error")
            return (data, all_sub_links)

        all_as = []
        for table in all_tables:
            links = table.find_all("a")
            all_as.append(links)
        if(all_as == []):
            data = constants["UNABLE_TO_FIND_ELEMENT"] + ": a"
            debugger_alert(data, "Error")
            return (data, all_sub_links)

        raw_links = []
        raw_links = list(itertools.chain.from_iterable(all_as))
        for link in raw_links:
            all_sub_links.append(str(link['href']))
        if(all_sub_links == []):
            data = constants["UNABLE_TO_FIND_ELEMENT"] + ": href"
            debugger_alert(data, "Error")
            return (data, all_sub_links)

        # print(all_sub_links)
        print("____GOT ALL SUBLINKS____")

        return (data, all_sub_links)
    except:
        data = constants["UNABLE_TO_SCRAP_PAGE"]
        debugger_alert(data, "Error")
        return (data, all_sub_links)

