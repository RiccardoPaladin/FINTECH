"""
Homework 2 - FA 595
Riccardo Paladin

Webscraping - 50 companies names and purposes
"""

import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

def obtain_web_info(url):
    '''
    Function to obtain infomation from the website
    :input: URL
    '''
    webscraping = []
    lines = []
    for _ in range(50):
        rec = requests.get(url)
        if rec.status_code == 200:
            soup = BeautifulSoup(rec.text, 'html.parser')
            for body in soup.find_all('body'):
                c = body.get_text()
                lines = c.split('\n')
                webscraping.append(lines)

        else:
            print('Error:', rec.status_code)
            break
    return webscraping

url = 'http://34.238.119.208:8000/random_company'
webscraping = obtain_web_info(url)

def name_purpose(webscraping):
    '''
    Function to organize in a dataset with names and purposes of the companies
    :input: information obtained from the webscraping
    '''
    names = []
    purposes = []
    dataset = pd.DataFrame()
    for i in range(50):
        for y in webscraping[i]:
            if 'Name:' in y:
                names.append(y)
        for x in webscraping[i]:
            if 'Purpose:' in x:
                purposes.append(x)
    df_names = pd.DataFrame(names)
    df_purposes = pd.DataFrame(purposes)
    dataset = pd.concat([df_names, df_purposes], axis = 1)
    dataset.columns = ['Names', 'Purposes']
    dataset['Names'] = dataset['Names'].str.replace('Name:', '')
    dataset['Purposes'] = dataset['Purposes'].str.replace('Purpose:', '')
    return dataset

dataset = name_purpose(webscraping)
dataset

#Save and store dataset
dataset.to_csv('webscrape_companies.csv')

if __name__ == "__main__":
    obtain_web_info()
    name_purpose()
