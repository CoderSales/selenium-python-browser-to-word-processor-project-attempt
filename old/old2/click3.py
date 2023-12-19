from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from urllib.parse import urlparse
driver = webdriver.Firefox()


# https://uilicious.com/blog/how-to-click-a-button-using-selenium/
button = driver.find_element(By.ID, "login-btn")
button.click()
