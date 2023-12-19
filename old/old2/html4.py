# https://www.geeksforgeeks.org/convert-html-source-code-to-json-object-using-python/

import xmltojson 
import json 
import requests

# url = "index.html"


# https://www.tutorialspoint.com/how-to-parse-local-html-file-in-python
# import beautifulsoup4 as bs4
import bs4
from bs4 import BeautifulSoup

# Load the HTML file
# https://stackoverflow.com/questions/36140147/unicodedecodeerror-on-byte-type
with open('index.html', 'r', encoding="ISO-8859-1") as file:
    html_content = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'lxml')

# Find the element to remove by its tag and remove it
# element_to_remove = soup.find('div')
# element_to_remove.extract()

# elements_to_find = soup.find('div')
# elements_to_find.


# div = soup.div
# div.['class']

# soup.p
# <p class="title"><b>The Dormouse's story</b></p>

# paragraph1=soup.p['class']
# print(paragraph1)

authors=soup.find(id="authors")
print(authors)

title=soup.title
# <title>The Dormouse's story</title>

title_name=soup.title.name
# u'title'

title_string=soup.title.string
# u'The Dormouse's story'

title_parent=soup.title.parent.name
# u'head'

paragraph=soup.p
# <p class="title"><b>The Dormouse's story</b></p>

paragraph_class=soup.p['class']
# u'title'

anchor=soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

all_anchors=soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

link3=soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


# Print the modified HTML



# print(soup.prettify())