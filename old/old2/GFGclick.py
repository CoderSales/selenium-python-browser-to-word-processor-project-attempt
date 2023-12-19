# /https://www.geeksforgeeks.org/click-element-method-selenium-python/
# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Firefox()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

import time
time.sleep(10)

# >B:<
# https://stackoverflow.com/questions/27112731/selenium-common-exceptions-nosuchelementexception-message-unable-to-locate-ele
driver = webdriver.Firefox()

driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
# B



# C
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.geeksforgeeks.org/")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Courses"))
    )
finally:
    driver.quit()
#c



# get element 
element = driver.find_element(By.LINK_TEXT, "Courses")

# click the element
element.click()
