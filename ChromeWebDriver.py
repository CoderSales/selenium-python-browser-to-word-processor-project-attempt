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

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()

