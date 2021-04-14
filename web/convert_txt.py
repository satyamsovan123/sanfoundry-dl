#!/usr/bin/env python3
import re
from bs4 import BeautifulSoup
import urllib.request
import ssl
import requests
import certifi
import os
from colorama import *

def convert_txt():
	#print(os.getcwd())
	url_lst = []
	with open("links.txt" , "r") as file:
		for line in file:
			if line.startswith("#"):
				pass
			else:
				url_lst.append(line)

	#print(url_lst)
	headers = {
		    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
		  }

	counter = 1
	#URL = url_lst[67]
	for URL in url_lst:
		print(Fore.BLUE + "Parsing : " + str(counter) + "/" + str(len(url_lst)) + " ---> " + URL)
		print(Style.RESET_ALL)
		page = requests.get(URL , headers = headers)
		soup = BeautifulSoup(page.content ,'html.parser')
		counter += 1

		f = re.search(r"^https://www.sanfoundry.com/(.*)/" , URL)
		file_name = "txt-sites/" + f[1]
		#print(file_name)

		with open(file_name + ".txt" , "w") as file:
		    file.write(soup.getText().strip())
		file.close()
