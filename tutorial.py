# Selenium Tutorial #1
# https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome() # https://stackoverflow.com/questions/76928765/attributeerror-str-object-has-no-attribute-capabilities-in-selenium

####
# https://learn.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get('https://bing.com')

element = driver.find_element(By.ID, 'sb_form_q')
element.send_keys('WebDriver')
element.submit()

time.sleep(1)
driver.quit()
####


from files.pathgetter import getPath, geturl
# Path = getPath()

goturl = geturl()

# driver = webdriver.Chrome(Path)
driver = webdriver.Chrome()



driver.get(goturl)
driver
print(driver.title)

search = driver.find_elements_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

html_stuff = driver.page_source

driver.quit()