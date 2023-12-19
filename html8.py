long_string="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
import xmltojson 
import json 
import requests
import pandas
import re
import time
import nltk
# time3=time.monotonic() # https://docs.python.org/3/library/time.html
url = "http://127.0.0.1:5500/"
headers = {'User-Agent': long_string } 
html_response = requests.get(url=url, headers = headers) 
with open("index.html", "r", encoding='ISO-8859-1') as html_file: 
    for index, i in enumerate(html_file):
        for index4, i4 in enumerate(i):
            if ("<" not in i4 and ">" not in i4 and "/" not in i4 and "osano" not in i4):
                # print(i)
                tokens = nltk.word_tokenize(i) # https://www.nltk.org/
                tagged = nltk.pos_tag(tokens) # new
                # for index2, token in enumerate(tokens):
                    # print(token)
                for index3, x in enumerate(tagged):
                    [one_tag, tag_type]=x
                    if tag_type=='NN':
                        if ("=" not in one_tag and ">" not in one_tag and "comma-separator" not in one_tag and "a2" not in one_tag and "_Ctrl" not in one_tag and "a1" not in one_tag):
                            if ("a4" not in one_tag and "a5" not in one_tag and "<" not in one_tag):
                                if ("mathstat" not in one_tag and "bse" not in one_tag and "div" not in one_tag):
                                    if ("%" not in one_tag and "amp" not in one_tag):
                                        print(one_tag)
