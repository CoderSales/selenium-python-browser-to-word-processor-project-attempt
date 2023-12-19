long_string="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
import xmltojson 
import json 
import requests
import pandas
import re
import time
import nltk
import regex

# Part 1: compile list1

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
                    i5new=i5.translation(translation_table2)
                list1.append(i5)
                # input("coninue?")
            # tagged = nltk.pos_tag(tokens) # new
            # for index3, x in enumerate(tagged):
            #     [one_tag, tag_type]=x
            #     if tag_type=='NN':
            #         print(one_tag)
# print(list1)

# Part 2: list1 -> list2:

# TODO: (1): Work on list1:
list2=[] # unpack list1 and make list2
for index,i in enumerate(list1):
    # print(i)


    # TODO: (2): Add translation_table3
    if not ( re.search("^''", i) ):
        # print(i)
        translation_table3={re.sub(r'[A-Za-z]',",",list1[index]): None}
        inew=i.translate(translation_table3)
    list2.append(inew)
# print(list2)

# Part 3: list2 -> list3:

list3=[]
for index, i in enumerate(list2):
    if (i != ','):
        # print(i)
        list3.append(i)
# print(list3)

# Part 4: list3 -> list4:
list4=[]
list_arguments=['{','}','``',':',';',',']
item='{'
# print(list_arguments[0])
for index, i in enumerate(list3):
    # for index2, i2 in enumerate(list_arguments):
    i2_0=item
    # print(i2_0)
    # print(i)
    # translation_table4={ord(f"{item}"):None}
    # i2new=item.translate(translation_table4)
    # print(i2new)

#     if not (re.search('', item) ):
#         list4.append(item)
# print(list4)


    if (i!='.' and i!= '{' and i!= '}'):
        list4.append(i)
# print(list4)

# Part 5: 
list5=[]
string1 = '():;!|[]?+&-'
for i in list4:
    # for index2, i2 in enumerate(string1):
    if ( i != string1[0] and i!= string1[1] and i!=string1[2] and i!=string1[3] and i!=string1[4] and i!=string1[5] and i!=string1[6] and i!=string1[7] and i!=string1[8] and i!=string1[9] and i!=string1[10] and i!=string1[11]):
        list5.append(i)
# print(list5)

# Part 6: 
list6=[]
for i in list5:
    if ( i != '``' ) :
        list6.append(i)
# print(list6)

# Part 7:
list7=[]
for i in list6:
    # if ( i != 'amp' and i!= 'class' and i!= 'osano' and i!= 'id' and i != 'iframe' and i!= 'style' and i != 'background-color' and i != 'white' and i != 'ACDL|Page|Brand' and i!= 'Code' and i!= 'Age' and i!= 'Id' and i!= 'Driver' and i!='Osano' and i!='Type' and i!= 'Promise' and i!='alloy' and i!='Variable|Page|Query_Param' and i!='true' and i!= 'href' and i!= 'text-align' and i!= 'javascript' and i[0:9]!=re.findall(r'ACDL|Page',i) != 'ACDL|Page' and i[0:13]!=re.findall(r'Variable|Page',i) != 'Variable|Page'):
    if ( i != 'amp' and i!= 'class' and i!= 'osano' and i!= 'id' and i != 'iframe' and i!= 'style' and i != 'background-color' and i != 'white' and i != 'ACDL|Page|Brand' and i!= 'Code' and i!= 'Age' and i!= 'Id' and i!= 'Driver' and i!='Osano' and i!='Type' and i!= 'Promise' and i!='alloy' and i!='Variable|Page|Query_Param' and i!='true' and i!= 'href' and i!= 'text-align' and i!= 'javascript'):
        list7.append(i)
# print(list7)

list8=[]
for i in list7:
    if ( i!= any(['mb-3', 'col-md-3', 'ga', 'Codes', 'divdivdiv', 'div', 'divbodyhtml']) ) :
        list8.append(i)
print(list8)

list9=[]
# https://docs.python.org/3/howto/regex.html
# First, run the Python interpreter, import the re module, and compile a RE:
p = re.compile('[0-9]')
p
re.compile('[0-9]')
# ('prop'+p+p)
# Now, you can try matching various strings against the RE [a-z]+.
for i in list8:
    m=re.match(r"(\d)(\d)",i)
    # print(m)
    if m != None:
        groups=m.groups()
        # print(groups)
        # for j in m:
        #     print(j)
    # if ( (\S+) (\d+) (\d+) ):
    # email = i
    # m2=re.search("")
        # print(i) 
    # if(  )
for i in list8:
    match=re.match(r"([a-z]+)(\d)(\d)", i)
    if (match):
        if i[0:4]=='prop':
            print('we got a prop!')
            print(i)
g