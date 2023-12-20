import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from unicodedata import normalize

#read all HTML tables from specific URL

tabs = pd.read_html('http://127.0.0.1:5500/')

#display total number of tables read

len(tabs)

#read HTML tables from specific URL with the word “Scotland” in them

tabs = pd.read_html('http://127.0.0.1:5500/')#, match='google')

#display total number of tables read

len(tabs)

print(tabs)

for a in tabs:
    # print(a)
    for i2,b in enumerate(a):
        if len(a)==2 and i2==0:
            print('start')
            print(a[i2],a[i2+1])
            print('end')
        else:
            print('else',i2)
        # print('i2:',i2)
        # print(b)
        # print('\n')
        # for c in range(b):
        #     print(c)