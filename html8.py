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
# re.sub(r'\d', '', my_string)
# loops:
with open("index.html", "r", encoding='ISO-8859-1') as html_file: 
    for index, i in enumerate(html_file):
        for index4, i4 in enumerate(i):
            i4new=i4.translate(translation_table)
            # print(i4new)
            # if ("<" not in i4 and ">" not in i4 and "/" not in i4 and "osano" not in i4):
            # print(i)
            tokens = nltk.word_tokenize(i) # https://www.nltk.org/
            tagged = nltk.pos_tag(tokens) # new
            # for index2, token in enumerate(tokens):
                # print(token)
            for index3, x in enumerate(tagged):
                [one_tag, tag_type]=x
                if tag_type=='NN':
                    # if ("=" not in one_tag and ">" not in one_tag and "comma-separator" not in one_tag and "a2" not in one_tag and "_Ctrl" not in one_tag and "a1" not in one_tag):
                    #     if ("a4" not in one_tag and "a5" not in one_tag and "<" not in one_tag):
                    #         if ("mathstat" not in one_tag and "bse" not in one_tag and "div" not in one_tag):
                    #             if ("%" not in one_tag and "amp" not in one_tag):
                    print(one_tag)

# "<"  ">"  "/" "osano"
# "="  ">" "comma-separator" "a2" "_Ctrl"  "a1"
# "a4"  "a5" "<" 
# "mathstat" "bse" "div"
# "%"  "amp"
