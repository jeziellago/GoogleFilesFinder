#!/usr/bin/python

# Google File Finder - Finished in Dec, 2016
# Powered by Jeziel Lago [jeziellago@gmail.com]

import os
import googlesearch

""" --------------------------------------------------------------------------- """
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

""" --------------------------------------------------------------------------- """
def listFilesFromResult(all_files, log):
	print('\nListing files URLs:\n')
	position = 1
	for url in all_files:
		url = cut_string(url,'&')
		if url[1:4] == 'url':
			url = url[7:len(url)]
			print('-------> ['+str(position)+"]   " + url)
			log.append(url)
			position += 1
	print('\n')
	return log

""" --------------------------------------------------------------------------- """
def saveResultsInFile(log_list):
	save_results = input("\n\n>> Do you want to save the results to a file? [Y/n] ")
	if save_results == '' or save_results == 'Y' or save_results == 'y':
		path_file = input("\n>> Enter the filename to save: ")
		if path_file != '':
			f = open(path_file,'w')
			n = 0
			for log in log_list:
				f.write("\n" + "[" + str(n) + "] "+ log)
				n = n + 1
			f.close()
			print("\nFile " + path_file + " saved!\n\n")

""" --------------------------------------------------------------------------- """
def downloadFiles(log_list):
	do_wget = input("\n>> Do you want download (with wget) all files? [Y/n] ")
	if do_wget == '' or do_wget == 'Y' or do_wget == 'y':
		dir_save = input("\n>> Enter dir for save the files: ")
		if dir_save != "":
			for log in log_list:
				os.system("wget " + log + " -P " + dir_save)
	else:
		do_wget = input("\n>> Do you want download (with wget) any file? [Y/n] ")
		if do_wget == '' or do_wget == 'Y' or do_wget == 'y':
			url_position = input("\n>> Enter the url position for download or 0 for exit (Ex.: 1,2,3...): ")
			while(int(url_position) > 0):
				dir_save = input("\n>> Enter dir for save the file: ")
				if dir_save != "":
					os.system("wget " + log_list[int(url_position)] + " -P " + dir_save)
				url_position = input("\n>> Enter the url position for download or 0 for exit (Ex.: 1,2,3...): ")
""" --------------------------------------------------------------------------- """
def printHeader():
	os.system("clear")
	print('================================================================')
	print('/                                                              /')
	print('/                GOOGLE FILE FINDER                            /')
	print('/                                               by Jeziel Lago /')
	print('================================================================')

""" --------------------------------------------------------------------------- """
def main():

	try:
		printHeader()
		# Input user search
		search = input("\n-> Enter a key word: ")
		log = []
		log.append("Key Word of File Search -> " + search + "\n\n")
	
		search = search.replace(" ","+")
		file_type = input("-> Enter the file type (Ex.: pdf, txt, docx): ")
		amount_results = int(input("-> Enter the max amount of results (Max = 1000000): "))
		
		# Start Search
		print('\n\n[-] Searching files in google...')
		search = googlesearch.search_google(search, amount_results, 1, file_type) 
		search.process()
		all_files = search.get_files()

		# Listing files from results
		log = listFilesFromResult(all_files, log)

		# Save Results
		saveResultsInFile(log)

		# Download files
		downloadFiles(log)
		
		print("\n\nFinish!\n")
	
	except KeyboardInterrupt:
		print('\n Files Finder closed..Thanks for use')

""" --------------------------------------------------------------------------- """

if __name__ == "__main__":
	main()
