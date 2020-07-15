#!/usr/bin/env python3
import os
import sys
from fpdf import FPDF 
import glob
import requests
from web import *

request = requests.get("http://www.gooogle.com")
if request.status_code != 200:
	print("\nThat's just you. You've forgot to turn on Wi-Fi / Mobile Data! Try again.\n")
	sys.exit()

elif len(sys.argv) - 1 == 0:
	print("\nWould you mind passing a sanfoundry-website (that has like a 1000 MCQs in it) ?\n")
	sys.exit()

elif "1000" not in sys.argv[1]:
	print("\nThe URL you've entered isn't currently supported in this version of sanfoundry-dl. I may or may not update !\n")
	sys.exit()

url = sys.argv[1]

def main():
	get_link.get_link(url)
	convert_txt.convert_txt()
	clean.clean()

	#os.chdir("web/txt-sites")
	
	if "result.txt" in os.listdir():
		os.remove("result.txt")

	all_files = glob.glob("*.txt")
	with open("result.txt" , "w") as result:
	    for file in all_files:
	        for line in open(file , "r"):
	            result.write(line)
	        result.write("\n********************************END-OF-A-PAGE********************************\n")
	    result.write("-----------------------------Best viewed in any Apple device------------------------------")
	print("\nYour result.txt file is ready and wasting some space inside desktop/sanfoundry-dl/web/txt-sites\n")

	old_fl = os.listdir()
	for file in old_fl:
		if file != "result.txt":
			os.remove(file)	

if __name__ == '__main__':
	main()

