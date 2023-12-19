# https://stackoverflow.com/questions/27112731/selenium-common-exceptions-nosuchelementexception-message-unable-to-locate-ele
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.co.uk/maps")
import time
time.sleep(2)
xpath='Reject all'
driver.find_element(By.XPATH, "xpath")
time.sleep(10000)

# frame_0 = driver.find_element_by_class_name('widget-consent-frame')
# frame_0 = driver.find_element_by_class_name('widget-consent-frame')

# frame_0 = driver.find_element(By.CLASS_NAME, "widget-consent-frame")
# driver.switch_to.frame(frame_0)

# agree_btn_0 = driver.find_element(By.ID,'introAgreeButton')
# agree_btn_0.click()
