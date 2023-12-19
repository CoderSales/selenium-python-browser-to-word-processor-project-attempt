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
        list_of_tags=[]
        for index, j in enumerate(i):
            absolute_index=index # index at < 
            if absolute_index<(len(i)-1):
                absolute_index+=1 # 1st letter after < (at 1st)
            assembled=''
            if absolute_index>52:
                print("line 23: absolute_index > 52=:",absolute_index)
            if absolute_index>=len(i)-1:
              break
            # if absolute_index:
            i_absolute_index=i[absolute_index]
            break_count=0
            if len(i)==36209:
                break_count+=1
                break
            if break_count==55:
                break_count+=1
                break
            break_count_escaped_zero=False
            if break_count!=0:
                break_count_escaped_zero=True
                # print("wow", "break_count_escaped_zero=",break_count_escaped_zero)
                # why does break_count never escape 0?
                # is it because:
                # not incremented?
            if i_absolute_index==";":
                print("it's a", i_absolute_index, "at",absolute_index,"and len(i) is:", len(i))
                print("line 49","break_count_escaped_zero=",break_count_escaped_zero)
            if i_absolute_index=="\n":
                print("line 55: new line char = i_absolute_index=",i_absolute_index)
            if i_absolute_index=="\n":
                i_absolute_index=" "
            new_char=i_absolute_index # could be problem
            if j=="<":
                been_in_end_tag_if_loop=False
                if been_in_end_tag_if_loop==False:
                    getoutofwhile=False
                while (new_char!="/" and new_char!=">"):
                    if getoutofwhile!=True:
                        if new_char!=">":
                            time1=time.monotonic() # https://docs.python.org/3/library/time.html
                            print("line 77: new_char is not equal to > new_char=",new_char)
                            print("line 78:", "i", i)
                            time2=time.monotonic()
                            print("time2:", time2,"time1:", time1)
                            if (time2-time1)>=1000:
                                break
                            if (time3-time1)>=1000:
                                break
                            if (time2-time1)>=10:
                                print("line 89:","times:",time3, time2, time1)
                                continue
                            if new_char=="!":
                                break
                            else:
                                continue
                print("line 101: assembled:",assembled)
                if assembled=='\n':
                    print("line 115: assembled=","\\n")
                list_of_tags.append(assembled)
                if new_char==("/" or ">"):
                    been_in_end_tag_if_loop=True
                    getoutofwhile=True

                    break


