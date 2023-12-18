# https://youtu.be/b5jt2bhSeXs?t=476
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# file_path = 'index.html'

# with open(file_path, 'r', encoding='ISO-8859-1')as html_file:
#     print(html_file.readlines())

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start
    
from bs4 import BeautifulSoup

# https://www.reddit.com/r/learnpython/comments/j553tn/error_trying_to_import_beautifulsoup_from_bs4/
# Had the same issue, however never had file named 'bs4.py' in my folder...but a file named "html.py"...

# https://youtu.be/b5jt2bhSeXs?t=476

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

file_path = 'index.html'

# with open(file_path, 'r', encoding='ISO-8859-1')as html_file:
    # print(html_file.readlines())
    # print('done')
html_file = open(file_path, 'r', encoding='ISO-8859-1')
# soup = BeautifulSoup(html_file, 'html.parser')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


html_doc=html_file
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())


document=soup
# https://stackoverflow.com/questions/7115022/how-do-i-enumerate-all-of-the-html-ids-in-a-document-with-javascript
# document.querySelectorAll('*[id]')
# document.getElementsByTagName("*")

# input_from_find = document.find_element_by_id()

# a=html_file.find_element_by_id("crossmark-widget")
# print(a)
for i in html_file:
    # input_from_find = i.find_element_by_id("crossmark-widget")
    # print(input_from_find)
    print(i)


with open('index.html', 'r', encoding='ISO-8859-1') as f:
    mylist = list(f)

#########
    
# https://docs.python.org/3/library/xml.dom.minidom.html#:~:text=Instead%2C%20xml.-,dom.,not%20support%20the%20official%20API.

import xml.dom.minidom

# document = """\
# <slideshow>
# <title>Demo slideshow</title>
# <slide><title>Slide title</title>
# <point>This is a demo</point>
# <point>Of a program for processing slides</point>
# </slide>

# <slide><title>Another demo slide</title>
# <point>It is important</point>
# <point>To have more than</point>
# <point>one slide</point>
# </slide>
# </slideshow>
# """


# document=open('html1.py', 'r', encoding='ISO-8859-1')
# dom = xml.dom.minidom.parseString(document)


text_file = 'index.html'
text_file = open(text_file)
print(type(text_file))
with open(text_file,"a+") as document: # 
#   r = op.write('\n Hi')
    print('hi2')
dom = xml.dom.minidom.parseString(document)



def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def handleSlideshow(slideshow):
    print("<html>")
    handleSlideshowTitle(slideshow.getElementsByTagName("title")[0])
    slides = slideshow.getElementsByTagName("slide")
    handleToc(slides)
    handleSlides(slides)
    print("</html>")

def handleSlides(slides):
    for slide in slides:
        handleSlide(slide)

def handleSlide(slide):
    handleSlideTitle(slide.getElementsByTagName("title")[0])
    handlePoints(slide.getElementsByTagName("point"))

def handleSlideshowTitle(title):
    print(f"<title>{getText(title.childNodes)}</title>")

def handleSlideTitle(title):
    print(f"<h2>{getText(title.childNodes)}</h2>")

def handlePoints(points):
    print("<ul>")
    for point in points:
        handlePoint(point)
    print("</ul>")

def handlePoint(point):
    print(f"<li>{getText(point.childNodes)}</li>")

def handleToc(slides):
    for slide in slides:
        title = slide.getElementsByTagName("title")[0]
        print(f"<p>{getText(title.childNodes)}</p>")

handleSlideshow(dom)


########

# https://www.geeksforgeeks.org/how-to-parse-local-html-file-in-python/

from bs4 import BeautifulSoup 
  
# Importing the HTTP library 
import requests as req 
  
# Requesting for the website 
# Web = req.get('index.html')


# # # # # # # # 

from bs4 import BeautifulSoup 
  
# Opening the html file 
HTMLFile = open("index.html", "r") 
  
# Reading the file 
index = HTMLFile.read() 
  
# Creating a BeautifulSoup object and specifying the parser 
S = BeautifulSoup(index, 'lxml') 
  
# Using the select-one method to find the second element from the li tag 
Tag = S.select_one('li:nth-of-type(2)') 
  
# Using the decompose method 
Tag.decompose() 
  
# Using the prettify method to modify the code 
# print(S.body.prettify()) 
