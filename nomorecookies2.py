# https://www.tutorialspoint.com/how-to-click-button-selenium-python
from selenium import webdriver
# set chromodriver.exe path
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("")
# https://www.selenium.dev/documentation/webdriver/elements/finders/
from selenium.webdriver.common.by import By
l =driver.find_elements(By.CLASS_NAME , 'fc-button-label')
# https://stackoverflow.com/questions/70203815/python-selenium-printing-results-as-selenium-webdriver-remote-webelement-webe
for i in l:
    if i.text=="Manage options":87
##################
l =driver.find_elements(By.CLASS_NAME , 'fc-slider-el')
# print(l[0])
import re
for index,i in enumerate(l):
    print(i.value_of_css_property('Use limited data to select advertising')) # issue: # TypeError: WebElement.value_of_css_property() missing 1 required positional argument: 'property_name'
    if index == 1:
        break
    # class="fc-preference-slider-label"
    l3=driver.find_elements(By.CLASS_NAME, "fc-preference-slider-container")
    l2 =driver.find_elements(By.CLASS_NAME , "fc-preference-slider-label")
    for index2, i2 in enumerate(l2):
        for char in i2.text:
            if char ==" ":
                continue
            else:
                if re.search("^Legitimate interest",i2.text):
                    i2.click()
                    break
###################
# class="fc-navigation-button-label"
l =driver.find_elements(By.CLASS_NAME , 'fc-navigation-button-label')
# class = fc-button-label
# https://stackoverflow.com/questions/70203815/python-selenium-printing-results-as-selenium-webdriver-remote-webelement-webe
for i in l:
    # print("Vendor?:", i)
    if i.text=="Vendor preferences":
        # print(i) # was issue
        i.click()
###################
l =driver.find_elements(By.CLASS_NAME , 'fc-slider-el')
for index,i in enumerate(l):
    if index == 1:
        break
    # class="fc-preference-slider-label"
    l3=driver.find_elements(By.CLASS_NAME, "fc-preference-slider-container")
    l2 =driver.find_elements(By.CLASS_NAME , "fc-preference-slider-label")
    for index2, i2 in enumerate(l2):
        for char in i2.text:
            if char ==" ":
                continue
            else:
                if re.search("^Legitimate interest",i2.text):
                    i2.click()
                    break

# class="fc-footer-buttons-container"
l =driver.find_elements(By.CLASS_NAME , 'fc-footer-buttons-container')
# print("line26:",l)
for i in l:
    print(i)
    # class="fc-button fc-confirm-choices fc-primary-button"
    l2 =driver.find_elements(By.CLASS_NAME , 'fc-button.fc-confirm-choices.fc-primary-button')
    for i2 in l2:
        if i2.text=="Confirm choices":
            i2.click()
###################
driver.quit()
