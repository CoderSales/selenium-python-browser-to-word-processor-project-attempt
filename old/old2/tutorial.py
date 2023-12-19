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

# element = driver.find_element(By.ID, 'sb_form_q')
# element.send_keys('WebDriver')
# element.submit()

element = driver.find_element(By.ID, 'W0wltc')



'<button id="W0wltc" class="tHlp8d" data-ved="0ahUKEwiAi-G_05mDAxWbUEEAHWFtDq8Q4cIICHk"><div class="QS5gu sy4vM" role="none">Reject all</div></button>'

time.sleep(300)
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


# https://stackoverflow.com/questions/21350605/python-selenium-click-on-button

# driver.find_element_by_css_selector('.button .c_button .s_button').click()
# clicker = driver.find('.button .c_button .s_button').click()




html_stuff = driver.page_source

driver.quit()