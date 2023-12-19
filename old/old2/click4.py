# https://www.tutorialspoint.com/how-to-click-button-selenium-python
from selenium import webdriver
#set chromodriver.exe path
driver = webdriver.Firefox()
#implicit wait
driver.implicitly_wait(0.5)
#maximize browser
driver.maximize_window()
#launch URL
driver.get("https://www.tutorialspoint.com/index.htm")
import time
time.sleep(1)

#identify element
# https://www.selenium.dev/documentation/webdriver/elements/finders/

from selenium.webdriver.common.by import By

l =driver.find_elements(By.CLASS_NAME , 'fc-button-label')
# class = fc-button-label
# https://stackoverflow.com/questions/70203815/python-selenium-printing-results-as-selenium-webdriver-remote-webelement-webe
for i in l:
    if i.text=="Manage options":
        print(i) # was issue
        i.click()
# print("Page title is: ")
# print(driver.title)

##################

l =driver.find_elements(By.CLASS_NAME , 'fc-slider-el')
# class = fc-button-label
print(l[0])
import re
for index,i in enumerate(l):#
    print(i)
    print(i.value_of_css_property('Use limited data to select advertising')) # issue: # TypeError: WebElement.value_of_css_property() missing 1 required positional argument: 'property_name'
    if index == 1:
        break
    #     print(i) # was issue
    #     i.click()

    # class="fc-preference-slider-label"
    l3=driver.find_elements(By.CLASS_NAME, "fc-preference-slider-container")
    l2 =driver.find_elements(By.CLASS_NAME , "fc-preference-slider-label")
    # print('##################################################\n#####\n####\n####\n####\n####\n####\n###')
    # for index3, i3 in enumerate(l3):
    #     tname=i3.tag_name
    #     l2 =driver.find_elements(By.CLASS_NAME , "fc-preference-slider-label")
    for index2, i2 in enumerate(l2):
        for char in i2.text:
            if char ==" ":
                continue
            else:
                # print(i2.text)
                # x=0
                if re.search("^Legitimate interest",i2.text):
                    # print(x)
                    # x+=1
                    # print("index",index)
                    i2.click()
                    break
                    # continue

        # if == :
        #     print(i2)
        #     i2.click()





###################

# driver.quit()
