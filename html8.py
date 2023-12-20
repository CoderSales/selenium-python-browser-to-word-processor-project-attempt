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
# print(list8)

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
prop_list=[]
for i in list8:
    match=re.match(r"([a-z]+)(\d)(\d)", i) # https://towardsdatascience.com/easiest-way-to-remember-regular-expressions-regex-178ba518bebd
    if (match):
        if i[0:4]=='prop':
            # print('we got a prop!')
            # print(i)
            prop_list.append(i)
# print(prop_list)
list9=[]
for i in list8:
    if i != any(prop_list):
        list9.append(i)
    # for j in prop_list:
    #     if i == j:
# print(list9)
unique_items_list9=set(list9)
# print(unique_items_list9)
list10=[]
for i in list9:
    if 'bse' not in i:
        list10.append(i)
# print(list10)
unique_items_list10=set(list10)
# print(unique_items_list10)
# reduction10to9=len(unique_items_list9)-len(unique_items_list10)
# print(reduction10to9) # 991
# print(len(unique_items_list10)) # 6255
list11=[]
for i in list10:
    if 'span' not in i:
        list11.append(i)
list11
unique_items_list11=set(list11)
# print(unique_items_list11)
reduction10to11=len(unique_items_list10)-len(unique_items_list11)
# print(reduction10to11) # 825
# print(len(unique_items_list11)) # 5430
list12=[]
for i in list11:
    if i != any(['types','div.content', 'SeriesKey', 'fixed-element','osano-cm-buttons']):
        # print(i)
        list12.append(i)
list12
unique_items_list12=set(list12)
# print(unique_items_list12)
reduction11to12=len(unique_items_list11)-len(unique_items_list12)
# print(reduction11to12) # 
# print(len(unique_items_list12)) # 
list13=[]
for i in list12:
    if i != any(['continue','async']):
        # print(i)
        list13.append(i)
list13
unique_items_list13=set(list13)
# print(unique_items_list13)
reduction12to13=len(unique_items_list12)-len(unique_items_list13)
# print(reduction12to13) # 0 ?
# print(len(unique_items_list13)) # 5430

found_list=[]
for i in list13:
    match=re.match(r"\'_*([A-Z])", i) # https://towardsdatascience.com/easiest-way-to-remember-regular-expressions-regex-178ba518bebd
    if (match):
        if i[0:5]=='\'__CF':
            print('we got a \'__CF !')
            # print(i)
            found_list.append(i)
# print(found_list)
list14=[]
for i in list13:
    if i != any(found_list):
        list14.append(i)
list14
unique_items_list14=set(list14)
# print(unique_items_list14)
reduction13to14=len(unique_items_list13)-len(unique_items_list14)
# print(reduction13to14) # 0 ?
# print(len(unique_items_list14)) # 5430



# if ACDL|
found_list=[]
for i in list14:
    match=re.match(r"ACDL\|([A-Z]*)", i) # https://towardsdatascience.com/easiest-way-to-remember-regular-expressions-regex-178ba518bebd
    if (match):
        if i[0:5]=='ACDL|':
            print('we got a ACDL| !')
            # print(i)
            found_list.append(i)
# print(found_list)
list15=[]
for i in list14:
    if i != any(found_list):
        list15.append(i)
list15
unique_items_list15=set(list15)
# print(unique_items_list15)
reduction14to15=len(unique_items_list15)-len(unique_items_list15)
# print(reduction14to15) # 0 ?
# print(len(unique_items_list15)) # 5430
len_list15=len(list15) # 44138
# print(len(list14)) #44138 # 37219
# print(len_list15) # 44138 # 27219

# Section: edit html to string:
# print('line246: type(list15)=',type(list15))
html_as_string=''.join(list15)

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        print('\n')

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
        print('\n')
    def handle_data(self, data):
        print("Encountered some data  :", data)
        print('\n')
parser = MyHTMLParser()
parser.feed(html_as_string)
