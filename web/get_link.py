#!/usr/bin/env python3
import re
from bs4 import BeautifulSoup
import urllib.request
import ssl
import requests
import certifi
import os
from colorama import *

def get_link(url):
	#page = urllib.request.urlopen("https://www.sanfoundry.com/1000-bioinformatics-questions-answers/")
	#soup = BeautifulSoup(page)
	URL = url
	headers = {
	    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
	  }

	page = requests.get(URL,headers = headers)
	soup = BeautifulSoup(page.content,'html.parser') 

	all_tables = soup.find_all("table")

	tab_ls = []
	for item in all_tables:
		links = item.find_all("a")
		#print(links)
		tab_ls.append((links))

	temp = []
	for tab in tab_ls:
		#print(tab)
		for link in tab:
			#print(link)
			temp.append(str(link))
	#print(len(temp))

	link_ls = []
	for link in temp:
		#print(link)
		pattern = re.search(r"^<a href=\"(.*)\"" , link)
		link_ls.append(pattern[1])

	os.chdir("web")
	with open("links.txt" , "w") as file:
		for link in link_ls:
			file.write(link)
			file.write("\n")
	file.close()

