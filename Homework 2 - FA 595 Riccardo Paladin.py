"""
Homework 2 - FA 595
Riccardo Paladin

Company analysis from website
"""

import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

url = 'http://34.238.119.208:8000/random_company'
rec = requests.get(url)

if rec.status_code == 200:
    print('success:' %f/rec.status_code)
else:
    print('error:' %f/ rec.status_code)

rec.headers['Content-Type']

soup1 = BeautifulSoup(rec.text, 'html.parser')
print("Title of the website is : ")
for title in soup1.find_all('title'):
    print(title.get_text())

#for recs in range(50):
    #recs = requests.get(url)
    #status = recs.status_code


print(soup1.get_text())

body = soup1.body
body
