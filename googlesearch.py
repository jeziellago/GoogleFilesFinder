import string
import sys
import re
import time
import requests
import myparser

class search_google:

    def __init__(self, word, limit, start, filetype):
        self.word = word
        self.files = ""
        self.results = ""
        self.totalresults = ""
        self.server = "www.google.com"
        self.userAgent = "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"
        self.quantity = "100"
        self.limit = limit
        self.counter = start
        self.filetype = filetype
  
    def do_search(self):
        try:
            #urly="http://" + self.server + "/search?num=" + self.quantity + "&start=" + str(self.counter) + "&hl=pt&meta=&q=%40\"" + self.word + "\""
			#urly="http://google.com.br/search?hl=pt&q=" + self.word + "&as_filetype=pdf"
            urly="https://www.google.com.br/search?hl=pt&q=sql" + self.word + "&as_filetype=" + self.filetype + "&gws_rd=ssl"
        except:
            print('Error...\n')
        try:
            r=requests.get(urly)
        except:
            print('Error...\n')
        self.results = str(r.content)
        self.totalresults += self.results


    def do_search_profiles(self):
        try:
            urly="http://" + self.server + "/search?num=" + self.quantity + "&start=" + str(self.counter) + "&hl=en&meta=&q=site:www.google.com%20intitle:\"Google%20Profile\"%20\"Companies%20I%27ve%20worked%20for\"%20\"at%20" + self.word + "\""
        except:
            print('Error...\n')
        try:
            r=requests.get(urly)
        except:
            print('Error...\n')
        self.results = r.content 

        #'&hl=en&meta=&q=site:www.google.com%20intitle:"Google%20Profile"%20"Companies%20I%27ve%20worked%20for"%20"at%20' + self.word + '"')
        self.totalresults += self.results

    def get_emails(self):
        rawres = myparser.parser(self.totalresults, self.word)
        return rawres.emails()

    def get_hostnames(self):
        rawres = myparser.parser(self.totalresults, self.word)
        return rawres.hostnames()

    def get_files(self):
        rawres = myparser.parser(self.totalresults, self.word)
        return rawres.fileurls(self.files)

    def get_profiles(self):
        rawres = myparser.parser(self.totalresults, self.word)
        return rawres.profiles()

    def process(self):
        while self.counter <= self.limit and self.counter <= 1000000:
            self.do_search()
            #more = self.check_next()
            time.sleep(1)
            print("\tSearching " + str(self.counter) + " results...")
            self.counter += 100

            
    def process_profiles(self):
        while self.counter < self.limit:
            self.do_search_profiles()
            time.sleep(0.3)
            self.counter += 100
            print("\tSearching " + str(self.counter) + " results...")
