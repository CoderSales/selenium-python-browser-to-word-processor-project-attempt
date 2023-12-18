long_string="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
import xmltojson 
import json 
import requests
import pandas
url = "http://127.0.0.1:5500/"
headers = {'User-Agent': long_string } 
html_response = requests.get(url=url, headers = headers) 
with open("index.html", "r", encoding='ISO-8859-1') as html_file: 
	for i in html_file:
          for index, j in enumerate(i):
            assembled=''
            start=0
            if j=="<":
                start=index+1
                continuation=start
                if j=="/" or ">":
                    # print('hi')
                    assembled=continuation
                    
                    print(assembled)
