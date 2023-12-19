long_string="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
import xmltojson 
import json 
import requests
import pandas
import re
import time
import nltk
time3=time.monotonic() # https://docs.python.org/3/library/time.html
url = "http://127.0.0.1:5500/"
headers = {'User-Agent': long_string } 
html_response = requests.get(url=url, headers = headers) 
with open("index.html", "r", encoding='ISO-8859-1') as html_file: 
    for i in html_file:
        tokens = nltk.word_tokenize(i) # https://www.nltk.org/
        for token in tokens:
            # print("line 17: tokens=", token)
            for token_char in token:
                if re.search("^''", token): # https://docs.python.org/3/library/re.html
                    print("line 20: token:", token, "starts with ''")
