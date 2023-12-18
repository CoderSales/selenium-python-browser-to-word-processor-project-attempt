# https://www.youtube.com/watch?v=ndwuUzgAiPY

import urllib.request

from bs4 import BeautifulSoup

import pandas as pd

from pandas import read_html

import html5lib

import time

url = 'index.html'

# html = urllib.request.urlopen(url).read()
# print(html)

tables_list = pd.io.html.read_html(url)
df=tables_list
# print(tables_list)

# for i,j in enumerate(tables_list):
#     print(j)
    # mf_list = tables_list[i]
    # https://youtu.be/b5jt2bhSeXs?t=391
    # sleep:
    # time.sleep(1)

print(type(df))
