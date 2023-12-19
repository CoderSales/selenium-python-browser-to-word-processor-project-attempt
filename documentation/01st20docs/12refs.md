# references

[fprint | GFG](https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/)

____

Search:

how to remove characters from a var in python

Result:

Code:

```python
def remove_commas(string):
   trans_table = {ord(',') : None, ord(':') : None, ord('.') : None}
   return string.translate(trans_table)

my_string = "In this string, there are no punctuation marks."

print(remove_commas(my_string))
```

[translate()](https://hostman.com/tutorials/how-to-delete-a-character-from-a-string-in-python/)

____

[string format](https://www.geeksforgeeks.org/python-string-format-method/)

____

[string formating using f strings and %](https://www.geeksforgeeks.org/string-formatting-in-python-using/?ref=lbp)

____
