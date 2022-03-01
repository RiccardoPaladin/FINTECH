"""
Homework 2 - FA 595
Riccardo Paladin

Webscraping - 50 companies names and purposes
"""

import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

webscraping = []
lines = []

#For loop to list the body of the website
for _ in range(50):
    url = 'http://34.238.119.208:8000/random_company'
    rec = requests.get(url)
    if rec.status_code == 200:
        soup = BeautifulSoup(rec.text, 'html.parser')
        for body in soup.find_all('body'):
            c = body.get_text()
            lines = c.split('\n')
            webscraping.append(lines)
    else:
        print('Error:', rec.status_code)

names = []
purposes = []

#For loop to create lists for names and purposes of the companies
for i in range(50):
    for y in webscraping[i]:
        if 'Name:' in y:
            names.append(y)
    for x in webscraping[i]:
        if 'Purpose:' in x:
            purposes.append(x)

#Organize results in dataset
df_names = pd.DataFrame(names)
df_purposes = pd.DataFrame(purposes)
dataset = pd.concat([df_names, df_purposes], axis = 1)
dataset.columns = ['Names', 'Purposes']
dataset['Names'] = dataset['Names'].str.replace('Name:', '')
dataset['Purposes'] = dataset['Purposes'].str.replace('Purpose:', '')
print(dataset)

#Save and store dataset
dataset.to_csv('webscraping_companies.csv')