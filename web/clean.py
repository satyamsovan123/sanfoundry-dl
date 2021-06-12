#!/usr/bin/env python3
import re
from bs4 import BeautifulSoup
import urllib.request
import ssl
import requests
import certifi
import os
from colorama import *

def clean():
#fls = "bioinformatics-questions-answers-protein-motifs-domain-prediction.txt"

	os.chdir("txt-sites")
	#print(os.getcwd())
	#print(os.getcwd())
	if (os.path.exists(os.getcwd() + "/.DS_Store")):
		os.remove(".DS_Store")
	'''
	if (os.path.exists(os.getcwd() + "/links.txt")):
		os.remove("links.txt")
	'''

	#print(os.listdir())

	fold_len = len(os.listdir())
	fold = os.listdir()
	i = 0
	while(i < fold_len):

		cts_fl = [] #cts_fl is contents of file in stored the list
		ques_ls = []
		opt_ls = []
		ans_ls = []
		exp_ls = []
		fls = fold[i]
		print(Fore.BLUE + "Cleaning ---> " + str(i) + " ---> " + fold[i])
		print(Style.RESET_ALL)
		with open(fls , "r", encoding="utf-8") as file:
			for line in file:
				cts_fl.append(line)
		file.close()

		for el in cts_fl:
			ques = re.findall(r"^(\d\d?. .*)\n" , el)
			if ques:
				ques_ls.append(str(ques).replace("[" , "").replace("]" , "").replace("'" , ""))
				continue

			opt = re.findall(r"^[   ]?(\(?[a-z]\) .*)\n" , el)
			if opt:
				opt_ls.append(str(opt).replace("[" , "").replace("]" , "").replace("'" , ""))
				continue

			ans = re.findall(r"^View Answer(Answer:  ?[a-z])\n" , el)
			if ans:
				ans_ls.append(str(ans).replace("[" , "").replace("]" , "").replace("'" , ""))
				continue

			exp = re.findall(r"^(Explanation.*)\n" , el)
			if exp:
				exp_ls.append(str(exp).replace("[" , "").replace("]" , "").replace("'" , ""))


		temp_ls = []
		str1 = ""  
		for ele in opt_ls:
			str1 = str1 + ele + " " 


		str2 = str1.split("a) ")
		if "" in str2:
			str2.remove("")

		for el in str2:
			temp_ls.append("a) " + el)

		final_ls = [i + "\n" + j + "\n" + k + "\n" + l +"\n" for i , j , k , l in zip(ques_ls , temp_ls , ans_ls , exp_ls)] 


		with open(fls , "w", encoding="utf-8") as f:
			for elem in final_ls:
				f.write("\n")
				f.write(elem)
			f.write("\n")
			if len(ques_ls) != len(ans_ls) != len(exp_ls):
				f.write("PSST! You better watch out, something's buggy above.")
		f.close()

		i += 1			
