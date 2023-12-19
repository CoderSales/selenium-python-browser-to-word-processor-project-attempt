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
# remove multiple elements
translation_table={ord("<"): None, ord(">"): None, ord("/"): None, re.sub(r'[A-Za-z]',",", "osano"): None, ord("="): None, ord(">"):None, re.sub(r'[A-Za-z]',",", "comma-separator"): None, re.sub(r'[A-Za-z]',",", "a2"): None, re.sub(r'[A-Za-z]',",", "_Ctrl"): None, re.sub(r'[A-Za-z]',",", "a1"): None, re.sub(r'[A-Za-z]',",", "a4"): None, re.sub(r'[A-Za-z]',",", "a5"): None, ord("<"): None, re.sub(r'[A-Za-z]',",", "mathstat"): None, re.sub(r'[A-Za-z]',",", "bse"): None, re.sub(r'[A-Za-z]',",", "div"): None, ord("%"): None, re.sub(r'[A-Za-z]',",", "amp"): None}
list1=[]
# loops:
with open("index.html", "r", encoding='ISO-8859-1') as html_file: 
    for index, i in enumerate(html_file):
        inew=i.translate(translation_table)
        tokens = nltk.word_tokenize(inew) # https://www.nltk.org/
        if(tokens!=[]):
            for i5 in tokens:
                if( re.search("osana",i5) ):
                    translation_table2={re.sub(r'[A-Za-z]'",",tokens):None}
                list1.append(i5)
                # input("coninue?")
            # tagged = nltk.pos_tag(tokens) # new
            # for index3, x in enumerate(tagged):
            #     [one_tag, tag_type]=x
            #     if tag_type=='NN':
            #         print(one_tag)
print(list1)
