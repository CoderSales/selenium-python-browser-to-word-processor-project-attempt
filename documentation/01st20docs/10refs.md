# references

[AttributeError: 'str' object has no attribute 'capabilities' in selenium](https://stackoverflow.com/questions/76928765/attributeerror-str-object-has-no-attribute-capabilities-in-selenium)

[httpx](https://www.python-httpx.org/)

[from selenium.webdriver.support import expected_conditions as EC](https://stackoverflow.com/questions/71365879/python-selenium-print-element-value-returns-session-xxx-element-xxx-and-n)

[4. Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html)

[Finding web elements](https://www.selenium.dev/documentation/webdriver/elements/finders/)

[AttributeError: 'WebDriver' object has no attribute 'find_element_by_xpath'](https://stackoverflow.com/questions/72754651/attributeerror-webdriver-object-has-no-attribute-find-element-by-xpath)

[Code Implementation with method click](https://www.tutorialspoint.com/how-to-click-button-selenium-python)

____

[selenium.webdriver.remote.webelement](https://www.selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html)

____

```python
import re
m = re.search('(?<=abc)def', 'abcdef')
m.group(0)
```

[re](https://docs.python.org/3/library/re.html)

____

```python
# import webdriver 
from selenium import webdriver 

# create webdriver object 
driver = webdriver.Firefox() 

# get geeksforgeeks.org 
driver.get("https://www.geeksforgeeks.org/") 

# get element 
element = driver.find_element_by_id("gsc-i-id2") 


# print width 
print(element.value_of_css_property('width')) 
```

[How to use value_of_css_property element method in Selenium Python ? | geeksforgeeks.prg](https://www.geeksforgeeks.org/value_of_css_property-element-method-selenium-python/)

____

aria_role

click() -> None

find_element(by='id', value=None) -> selenium.webdriver.remote.webelement.WebElement

find_elements(by='id', value=None) -> List[selenium.webdriver.remote.webelement.WebElement]

get_attribute(name) -> str | None[str, None]

get_dom_attribute(name) -> str

get_property(name) -> str | bool | selenium.webdriver.remote.webelement.WebElement | dict[str, bool, selenium.webdriver.remote.webelement.WebElement, dict]

id
    
    Internal ID used by selenium.

is_selected() → bool
    
    Returns whether the element is selected.

    Can be used to check if a checkbox or radio button is selected.

submit()

tag_name

text

value_of_css_property(property_name)

[selenium.webdriver.remote.webelement | selenium | documentation](https://www.selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html)

____

[Python RegEx](https://www.w3schools.com/python/python_regex.asp)

[Python RegEx | search](https://www.w3schools.com/python/python_regex.asp#search)
