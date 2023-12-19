# https://chromedriver.chromium.org/getting-started

# Error 1:
# AttributeError: 'WebDriver' object has no attribute 'find_element_by_name'
# Fix 1: | https://stackoverflow.com/questions/72773206/selenium-python-attributeerror-webdriver-object-has-no-attribute-find-el
# Selenium just removed that method in version 4.3.0
# You now need to use:
# driver.find_element("name", "q")



import time

from selenium import webdriver

browser = webdriver.Chrome() # https://stackoverflow.com/questions/76928765/attributeerror-str-object-has-no-attribute-capabilities-in-selenium



# driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/');

time.sleep(5) # Let the user actually see something!

# search_box = driver.find_element_by_name('q')
search_box = driver.find_element("name", "q")

# >A<:
# element = driver.find_element(By.ID, 'sb_form_q')
# element.send_keys('WebDriver')
# element.submit()
from selenium import webdriver
from selenium.webdriver.common.by import By
element = driver.find_element(By.ID, 'W0wltc')



'<button id="W0wltc" class="tHlp8d" data-ved="0ahUKEwiAi-G_05mDAxWbUEEAHWFtDq8Q4cIICHk"><div class="QS5gu sy4vM" role="none">Reject all</div></button>'





# >B<:
# https://stackoverflow.com/questions/21350605/python-selenium-click-on-button


# driver.find_element_by_css_selector('.button .c_button .s_button').click()
# driver.find_element_by_css_selector('.LC20lb .MBeuO .DKV0Md').click()
# element = driver.find_element(By.ID, 'W0wltc')

# clicker = driver.find_element_by_css_selector('.button .c_button .s_button').click()
clicker = driver.find_element(By.ID, 'W0wltc').click()

# <button id="W0wltc" class="tHlp8d" data-ved="0ahUKEwiAi-G_05mDAxWbUEEAHWFtDq8Q4cIICHk"><div class="QS5gu sy4vM" role="none">Reject all</div></button>


search_box.send_keys('ChromeDriver')

search_box.submit()
time.sleep(5)
# print(driver.page_source) # works
time.sleep(5)
# driver.find_element_by_css_selector('.LC20lb .MBeuO .DKV0Md').click()
# driver.find_element('.LC20lb.MBeuO.DKV0Md').click()

# https://selenium-python.readthedocs.io/locating-elements.html

driver.find_element(By.CLASS_NAME,'.LC20lb.MBeuO.DKV0Md').click()
element2=driver.find_element(By.CLASS_NAME,'.LC20lb.MBeuO.DKV0Md')

# element.click()
element2.click()


# >C:<
# https://www.geeksforgeeks.org/click-element-method-selenium-python/
# click
# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
 
# create webdriver object
driver = webdriver.Firefox()
 
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
 
# get element 
element = driver.find_element(By.LINK_TEXT, "Courses")
 
# click the element
element.click()


time.sleep(20000) # Let the user actually see something!

# driver.quit()

# error: AttributeError: 'WebDriver' object has no attribute 'find_element_by_css_selector'
# https://stackoverflow.com/questions/72854116/selenium-attributeerror-webdriver-object-has-no-attribute-find-element-by-cs
# Answer: The individual methods find_element_by_* have been replaced by find_element

