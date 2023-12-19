long_string="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
import xmltojson 
import json 
import requests
import pandas
import re
import time
time3=time.monotonic() # https://docs.python.org/3/library/time.html
url = "http://127.0.0.1:5500/"
headers = {'User-Agent': long_string } 
html_response = requests.get(url=url, headers = headers) 
with open("index.html", "r", encoding='ISO-8859-1') as html_file: 
    for i in html_file:
        list_of_tags=[]
        for index, j in enumerate(i):
            # print(j) # each letter
            # tag_char_index=j
            absolute_index=index # index at < 
            if absolute_index<(len(i)-1):
                absolute_index+=1 # 1st letter after < (at 1st)
            assembled=''
            print(absolute_index)
            if absolute_index>=len(i)-1:
              break
            # if absolute_index:
            i_absolute_index=i[absolute_index]
            # if absolute_index>=50:
            #     print("i_absolute_index>50 and i_absolute_index=",i_absolute_index)
            # if absolute_index==54:
            #     print("i[54]=",i[54])
            # if absolute_index>25323:
            #     print("len(i)=",len(i))
            #     print("absolute_index exceeded 25323, absolute_index=",absolute_index)
            break_count=0
            # print("line 27: break_count=",break_count)
            if len(i)==36209:
                # print("line 29: break_count=",break_count)
                break_count+=1
                # print("line 31: break_count=",break_count)
                break
            # print("line 33: break_count=",break_count)
            if break_count==55:
                # print("line 35: break_count=",break_count)
                break_count+=1
                # print("line 37: break_count=",break_count)
                break
            print("line 39: break_count=",break_count)
            # if break_count==0:
            #     print("line 41: why is break_count still =",break_count,"?") # = 0 ?
            break_count_escaped_zero=False
            if break_count!=0:
                break_count_escaped_zero=True
                print("wow", "break_count_escaped_zero=",break_count_escaped_zero)
                # why does break_count never escape 0?
                # is it because:
                # not incremented?
            if i_absolute_index==";":
                print("it's a", i_absolute_index, "at",absolute_index,"and len(i) is:", len(i))
                print("line 49","break_count_escaped_zero=",break_count_escaped_zero)
            # print("line 52: new_char=i_absolute_index=",i_absolute_index)
            # print("line 53 continues 52:","at",absolute_index,"and len(i) is:", len(i))
            if i_absolute_index=="\n":
                print("line 55: new line char = i_absolute_index=",i_absolute_index)
            # print("line 56:", "problem identified:", "how to deal with new line, '\\n' character ?")
            # print("line 57:", "answer is:", "add a backslash escape character: '\\' before '\\n' . ")
            # print("line 58:", "and incidentally,", "before '\\' backslash character possibly,")
            # print("line 59:", "or possibly not relevant here.")
            if i_absolute_index=="\n":
                i_absolute_index=" "
            new_char=i_absolute_index # could be problem
            if j=="<":
                been_in_end_tag_if_loop=False
                # define getoutofwhile somewhere
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
                            continue
                            # if i == :
                            if new_char=="!":
                                print("line 78:", new_char)
                                break
                            if absolute_index <= len(i)-1:
                                old_char=i[absolute_index-1]
                            if old_char==new_char:
                                char_two_ago=i[absolute_index-2]
                                if new_char==char_two_ago:
                                    print("triple char")
                                    break
                            # #old:# print(new_char!=("/" or ">"))
                            new_char=i_absolute_index
                            assembled+=new_char
                            absolute_index+=1
                            print(new_char)
                            new_char=i_absolute_index
                print("line 101: assembled:",assembled)
                list_of_tags.append(assembled)
                if new_char==("/" or ">"):
                    # #old:# continue
                    been_in_end_tag_if_loop=True
                    getoutofwhile=True
                    break










            #     while j in re.search('[a-z][A-Z]'): # error
            #         print('hi')
            #         letter=i[continuation]
            #         print(letter)
            #         assembled+=letter
            #         continuation+=1
            # # else:
            # print(assembled)
