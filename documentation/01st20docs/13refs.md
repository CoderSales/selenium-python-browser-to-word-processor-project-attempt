# references

____

3 string formatting f print style pages:

https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/

https://www.geeksforgeeks.org/python-string-format-method/

https://www.geeksforgeeks.org/string-formatting-in-python-using/?ref=lbp

____

trying to implement

substring != regex

using:

https://docs.python.org/3/library/re.html

https://www.w3schools.com/python/python_regex.asp

https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/

____

any

https://www.programiz.com/python-programming/methods/built-in/any

____

regex implementations

Python has two major implementations, the built in re and the regex library.

https://www.google.com/search?q=different+impolementations+of+regex+in+python&rlz=1C1YTUH_enIE1084IE1084&oq=different+impolementations+of+regex+in+python&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDU4NDlqMWo3qAIAsAIA&sourceid=chrome&ie=UTF-8

https://en.wikipedia.org/wiki/Comparison_of_regular_expression_engines#:~:text=Python%20has%20two%20major%20implementations,re%20and%20the%20regex%20library.&text=Ruby%201.8%2C%20Ruby%201.9%2C%20and,Onigmo%2C%20a%20fork%20from%20Oniguruma.&text=The%20primary%20regex%20crate%20does%20not%20allow%20look%2Daround%20expressions.

____

Google Search String:

regex library python

https://www.google.com/search?q=regex+library+python&rlz=1C1YTUH_enIE1084IE1084&oq=regex+library+python&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yCAgFEAAYFhgeMggIBhAAGBYYHjIGCAcQRRg80gEINjE1OWowajeoAgCwAgA&sourceid=chrome&ie=UTF-8

```bash
pip install regex
```

https://pypi.org/project/regex/

____

Google Search String

regex python library documentation

https://www.google.com/search?q=regex+python+library+documentation&rlz=1C1YTUH_enIE1084IE1084&oq=regex+python+library+documentation&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhge0gEIODI5N2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8

```text
First, run the Python interpreter, import the re module, and compile a RE:
```

```python
import re
p = re.compile('[a-z]+')
p
re.compile('[a-z]+')
```

```text
Now, you can try matching various strings against the RE [a-z]+.
```

https://docs.python.org/3/howto/regex.html

____

```text
Now, let’s try it on a string that it should match, such as tempo. In this case, match() will return a match object, so you should store the result in a variable for later use.
```

```python
m = p.match('tempo')
m
<re.Match object; span=(0, 5), match='tempo'>
```

```text
Now you can query the match object for information about the matching string. Match object instances also have several methods and attributes; the most important ones are:
```

```text
Method/Attribute | Purpose

group() | Return the string matched by the RE

start() | Return the starting position of the match

end() | Return the ending position of the match

span() | Return a tuple containing the (start, end) positions of the match
```
____

Match objects always have a boolean value of True.

https://docs.python.org/3/library/re.html#match-objects

____

Google Search String

how to use regex python

https://www.google.com/search?q=how+to+use+regex+python&rlz=1C1YTUH_enIE1084IE1084&oq=how+to+use+regex+python&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yCAgFEAAYFhgeMggIBhAAGBYYHjIICAcQABgWGB4yCAgIEAAYFhgeMggICRAAGBYYHtIBCDUwMTNqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8#vhid=6JLknBDWvJChSM&vssid=l

regex that fixed issue:

[towardsdatascience](https://towardsdatascience.com/easiest-way-to-remember-regular-expressions-regex-178ba518bebd)

____

other regex

docs

https://docs.python.org/3/library/re.html#match-objects

gentler

Regular Expression HOWTO

https://docs.python.org/3/howto/regex.html#regex-howto

____

Google Search String for above

regex python library documentation

https://www.google.com/search?q=regex+python+library+documentation&rlz=1C1YTUH_enIE1084IE1084&oq=regex+python+library+documentation&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhge0gEIODI5N2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8

____

Search String

python list each element in a list

```text
Python's *for* and *in* constructs are extremely useful, and the first use of them we'll see is with lists. The *for* construct -- for var in list -- is an easy way to look at each element in a list (or other collection). Do not add or remove from the list during iteration.
```

https://www.google.com/search?q=python+list+each+element+in+a+list&rlz=1C1YTUH_enIE1084IE1084&oq=python+list+each+element+in+a+list&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIGCAQQRRhA0gEIOTA0M2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8

https://developers.google.com/edu/python/lists#:~:text=Python's%20*for*%20and%20*in,from%20the%20list%20during%20iteration.

____

search

python list each unique element in a list

https://www.google.com/search?q=python+list+each+unique+element+in+a+list&newwindow=1&sca_esv=592323233&rlz=1C1YTUH_enIE1084IE1084&sxsrf=AM9HkKn0yeHWwuMSBVlT-IrCyF0Y6O3B4Q%3A1703025670775&ei=BhyCZcv2Lp7ThbIPha6e6Aw&ved=0ahUKEwjLkZmByZyDAxWeaUEAHQWXB80Q4dUDCBA&uact=5&oq=python+list+each+unique+element+in+a+list&gs_lp=Egxnd3Mtd2l6LXNlcnAiKXB5dGhvbiBsaXN0IGVhY2ggdW5pcXVlIGVsZW1lbnQgaW4gYSBsaXN0MggQABiABBiiBDIIEAAYgAQYogRImx9Q6BRYsRxwAXgBkAEAmAFXoAH8A6oBATe4AQPIAQD4AQHCAgoQABhHGNYEGLADwgIHECMYsAIYJ8ICChAhGKABGMMEGArCAggQIRigARjDBOIDBBgAIEGIBgGQBgg&sclient=gws-wiz-serp

```text
1. Python Set() to Get Unique Values from a List
set(input_list_name)
list(set-name)
list_inp = [100, 75, 100, 20, 75, 12, 75, 25] set_res = set(list_inp) print("The unique elements of the input list using set():\n") list_res = (list(set_res)) for item in list_res: print(item)
```

[Get Unique Values From a List in Python](https://www.digitalocean.com/community/tutorials/get-unique-values-from-a-list-in-python)

```python
set(input_list_name)
```

____

python html parser

https://www.google.com/search?q=python+html+parser&rlz=1C1YTUH_enIE1084IE1084&oq=python+html+parser&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDI0NTVqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8

```python
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
```

The output will then be:

Encountered a start tag: html
Encountered a start tag: head
Encountered a start tag: title
Encountered some data  : Test
Encountered an end tag : title
Encountered an end tag : head
Encountered a start tag: body
Encountered a start tag: h1
Encountered some data  : Parse me!
Encountered an end tag : h1
Encountered an end tag : body
Encountered an end tag : html

https://docs.python.org/3/library/html.parser.html

____

unpack list to string

https://www.google.com/search?q=unpack+list+to+string&rlz=1C1YTUH_enIE1084IE1084&oq=unpack+list+to+string&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQIxgnGIAEGIoFMggIAhAAGBYYHjIICAMQABgWGB4yDQgEEAAYhgMYgAQYigUyDQgFEAAYhgMYgAQYigXSAQg1MTcyajBqOagCALACAA&sourceid=chrome&ie=UTF-8

Python - Unpack lists and join into a string

StackOverflow

https://stackoverflow.com/questions/30315880/python-unpack-lists-and-join-into-a-string

____

You can use + to join two lists, and join to join them.

```python

brands = ["google", "apple", "intel", "qualcomm"]
otherBrands = ["nike", "reebok", "puma"]

print ":".join(brands + otherBrands)
```

https://stackoverflow.com/questions/30315880/python-unpack-lists-and-join-into-a-string

____

search:

join all items in a list

https://www.google.com/search?q=join+all+items+in+a+list&rlz=1C1YTUH_enIE1084IE1084&oq=join+all+items+in+a+list&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIMCAEQABgUGIcCGIAEMgwIAhAAGBQYhwIYgAQyCAgDEAAYFhgeMggIBBAAGBYYHjIICAUQABgWGB4yCAgGEAAYFhgeMggIBxAAGBYYHjIICAgQABgWGB4yDQgJEAAYhgMYgAQYigXSAQg2NTU5ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8

```python
a = ['a', 'b', 'c']
res = "".join(a)
```

https://stackoverflow.com/questions/13174468/how-do-you-join-all-items-in-a-list

____

tried code, but ultimately unused:

```python
import html5lib
with open("mydocument.html", "rb") as f:
    document = html5lib.parse(f)
```

https://github.com/html5lib/html5lib-python

____

https://www.google.com/search?q=pandas+html+table&rlz=1C1YTUH_enIE1084IE1084&oq=pandas+html&gs_lcrp=EgZjaHJvbWUqDAgAEAAYFBiHAhiABDIMCAAQABgUGIcCGIAEMgYIARBFGDkyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyBggGEEUYQTIGCAcQRRg80gEIMzIxMmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8

https://pandas.pydata.org/docs/reference/api/pandas.read_html.html

____

pandas:

pip install lxml

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from unicodedata import normalize

#read all HTML tables from specific URL

tabs = pd.read_html(‘https://int.soccerway.com/teams/rankings/fifa/’)

#display total number of tables read

len(tabs)

#read HTML tables from specific URL with the word “Scotland” in them

tabs = pd.read_html(‘https://int.soccerway.com/teams/rankings/fifa/’,

      match=’Scotland’)

#display total number of tables read

len(tabs)

pip3 install pandas

import pandas as pd 

df_list = pd.read_html(html) 

print(len(df_list))

print(df_list[0])

dfs = pd.read_html(URL)

file_path = ‘‘table.html’

with open(file_path, ‘r’) as f:

 dfs = pd.read_html(f.read())

dfs[0]

____

above from:

https://scrapingrobot.com/blog/pandas-read-html/

____

matplotlib install

https://www.google.com/search?q=matplotlib+install&rlz=1C1YTUH_enIE1084IE1084&oq=matplotlib+install&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIGCAcQRRhB0gEIMzI5MmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8

python -m pip install -U pip
python -m pip install -U matplotlib

https://matplotlib.org/stable/users/installing/index.html


____

pandas.DataFrame.to_html

https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html

____

earlier reference:

how to remove characters from a var in python

To remove a character from a string in Python, you can use the translate() method. The method takes a dictionary or translation table as input and replaces characters in the string based on the provided arguments. To remove a character, you can specify an empty string as the value for that character.

https://www.google.com/search?q=how+to+remove+characters+from+a+var+in+python&rlz=1C1YTUH_enIE1084IE1084&oq=how+to+remove+characters+from+a+var+in+python&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgHGB4yDQgCEAAYhgMYgAQYigUyDQgDEAAYhgMYgAQYigUyDQgEEAAYhgMYgAQYigUyDQgFEAAYhgMYgAQYigUyBggGEEUYQNIBCTE0NDk4ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8

https://hostman.com/tutorials/how-to-delete-a-character-from-a-string-in-python/

https://www.nltk.org/

____