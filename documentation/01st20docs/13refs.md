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
