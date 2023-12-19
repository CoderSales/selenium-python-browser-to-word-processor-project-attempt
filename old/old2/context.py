# https://stackoverflow.com/questions/48620526/how-to-use-webdriver-as-context-manager
from selenium import webdriver

# with webdriver.Chrome() as wd:
#     res = wd.get('https://stackoverflow.com/questions/')
#     print(res.page_source)



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
# import urlparse
from urllib.parse import urlparse




driver = webdriver.Firefox()
search_term = input("What is your search term?: ")
url = "https://www.google.co.uk/search?client=ubuntu&channel=fs&q="

googurl = url+search_term

driver.get(googurl)
soup = BeautifulSoup(driver.page_source, features="lxml")


# webdriver.Firefox().get('https://stackoverflow.com/questions/').page_source
source=driver.page_source
import time
time.sleep(1)

# https://www.educative.io/answers/beautiful-soup-prettify
soup2 = BeautifulSoup(source, 'html.parser')
nice=soup2.prettify()
print(nice)
time.sleep(2)
