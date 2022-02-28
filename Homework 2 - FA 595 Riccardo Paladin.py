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
    print('success:', rec.status_code)
else:
    print('error:' , rec.status_code)

rec.headers['Content-Type']

soup = BeautifulSoup(rec.text, 'html.parser')
print("Title of the website is : ")
for title in soup.find_all('title'):
    print(title.get_text())

#for recs in range(50):
    #recs = requests.get(url)
    #status = recs.status_code

for body in soup.find_all('body'):
    print(body.get_text())

for body in soup.find_all('body'):
    c = body.get_text()

lines = c.split('\n')
lines

name = lines[4]
name
name1 = name.split(':')
name1[1] #name of the company
purpose = lines[7]
purpose
purpose1 = purpose .split(':')
purpose1[1]  #purpose of the company
data = pd.DataFrame({'Name':[name1[1]], 'Purpose':[purpose1[1]]})
data

for _ in range(50):
    url = 'http://34.238.119.208:8000/random_company'
    rec = requests.get(url)
    soup = BeautifulSoup(rec.text, 'html.parser')
    for body in soup.find_all('body'):
        c = body.get_text()
        lines = c.split('\n')
        name = lines[4]
        name1 = name.split(':')
        names = name1[1]
        data1 = pd.DataFrame({'Name': [name1[1]]})
        data1

for _ in range(50):
    lines2 = []
    url = 'http://34.238.119.208:8000/random_company'
    rec = requests.get(url)
    soup = BeautifulSoup(rec.text, 'html.parser')
    for body in soup.find_all('body'):
        c = body.get_text()
        lines2 = c.split('\n')
        lines2 = ''.join([x for x in lines2])

for _ in range(50):
    lines2 = []
    url = 'http://34.238.119.208:8000/random_company'
    rec = requests.get(url)
    soup = BeautifulSoup(rec.text, 'html.parser')
    for body in soup.find_all('body'):
        c = body.get_text()
        lines2 = c.split('\n')
        print(lines2)


print(soup1.get_text())

soup.find_all('li')