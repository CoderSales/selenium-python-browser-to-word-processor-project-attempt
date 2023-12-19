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
    for index, i in enumerate(html_file):
        tokens = nltk.word_tokenize(i) # https://www.nltk.org/
        for index2, token in enumerate(tokens):
            # print("line 17: tokens=", token)
            for index3, token_char in enumerate(token):
                # if re.search("^''", token): # https://docs.python.org/3/library/re.html
                # print("line 20: token:", token, "starts with ''")
                # for index4, character in enumerate(token):
                if token_char!="'":
                    print(token_char)
                    print(token)
