#!/usr/bin/python

# Google File Finder - Finished in Dec, 2016
# Powered by Jeziel Lago [jeziellago@gmail.com]

import os
from libs import *

try:
	os.system("clear")
	def cut_string(text, limit):
		i = 0
		while i > -1:
			s = str(text[i:(i+1)])
			i = i + 1
			if s == limit:
				text = text[0:i-1]
				i = -1
			if i > len(text):
				i = -1
		return text
	
	""" ---------------------Principal--------------------------------"""
	
	print('================================================================')
	print('/                                                              /')
	print('/                GOOGLE FILE FINDER                            /')
	print('/                                               by Jeziel Lago /')
	print('================================================================')
	
	search = raw_input("\n-> Enter a key word: ")
	log = []
	log.append("Key Word of File Search -> " + search + "\n\n")
	
	search = search.replace(" ","+")
	file_type = raw_input("-> Enter the file type (Ex.: pdf, txt, docx): ")
	amount_results = input("-> Enter the max amount of results (Max = 1000000): ")
	print('\n\n[-] Searching files in google...')
	search = googlesearch.search_google(search, amount_results, 1, file_type) 
	search.process()

	all_files = search.get_files()

	print('\nListing files URLs:\n')
		
	p = 0
	
	while p < len(all_files):
		url = all_files[p]
		url = cut_string(url,'&')
			
		if url[1:4] == 'url':
			url = url[7:len(url)]
			print('----------> ' + url)
			log.append("\n" + url)
		p = p + 1


	print('\n')
	
	try:
		save_results = raw_input("\n\n>> Do you want to save the results to a file? [Y/n] ")
		if save_results == '' or save_results == 'Y' or save_results == 'y':
			path_file = raw_input("\n>> Enter the path to save the file: ")
			if path_file != '':
				f = open(path_file,'w')
				for n in range(0,len(log)):
					f.write(log[n])
				f.close()
				print("\nFile " + path_file + " saved!\n\n")
		do_wget = raw_input("\n>> Do you want download (with wget) the files? [Y/n] ")
		if do_wget == '' or do_wget == 'Y' or do_wget == 'y':
			dir_save = raw_input("\n>> Enter dir for save the files: ")
			if dir_save != "":
				for n in range(1,len(log)):
					os.system("wget " + log[n] + " -P " + dir_save)
			
		
				
	except:
		print("\nError in saving file " + path_file)
	
	print("\n\nAction finished!\n")
	
	

except KeyboardInterrupt:
	print('\n Files Finder closed..Thanks for use')
