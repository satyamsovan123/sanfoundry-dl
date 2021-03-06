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

		ques_ls = []
		opt_ls = []
		ans_ls = []
		exp_ls = []
		fls = fold[i]
		print(Fore.BLUE + "Cleaning ---> " + str(i) + " ---> " + fold[i])
		print(Style.RESET_ALL)
		with open(fls , "r") as file:
			# total_content contains all the contents of the file
			total_content = file.read()

		# regex to extract questions from the file
		questions = re.findall(
            	 r"^\d\d?\.([\w\W]*?\??)\n(?:a\)([\w\W]*?)\n)(?:b\)([\w\W]*?)\n)?(?:c\)([\w\W]*?)\n)?(?:d\)([\w\W]*?)\n)?(?:e\)([\w\W]*?)\n)?View Answer ?(Answer: *\w)\nExplanation: ?([\w\W]*?)\n\n", total_content, re.MULTILINE)
        	for question_data in questions:
            		question = question_data[0].strip().replace('advertisement', '')
            		max_index = len(question_data)
            		answer = question_data[-2].strip().replace('advertisement', '')
			explanation = question_data[-1].strip().replace('advertisement', '')
            		options = [question_data[i].strip().replace('advertisement', '') for i in range(
                	 1, max_index - 2) if question_data[i] and question_data[i] != '']
            		ques_ls.append(question)
            		options_string = '\n'.join(
                	 [chr(ord('A') + i) + '. ' + option for i, option in enumerate(options)])
            		opt_ls.append(options_string)
            		ans_ls.append(answer)
			exp_ls.append(explanation)

		
		final_ls = [i + "\n" + j + "\n" + k + "\n" + l +"\n" for i , j , k , l in zip(ques_ls , opt_ls , ans_ls , exp_ls)] 


		with open(fls , "w") as f:
			for elem in final_ls:
				f.write("\n")
				f.write(elem)
			f.write("\n")
			if len(ques_ls) != len(ans_ls) != len(exp_ls):
				f.write("PSST! You better watch out, something's buggy above.")
		f.close()

		i += 1			
