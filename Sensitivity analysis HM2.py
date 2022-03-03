"""
Analyze best and worst companies based on their purposes
"""
import pandas as pd
import numpy as np
from textblob import TextBlob

data = pd.read_csv(r'/Users/riccardopaladin/Desktop/webscrape_companies.csv')
data

#With blob Test:
for i in data['Purposes']:
    analysis = []
    blob = TextBlob(str(i))
    s = blob.sentiment
    analysis.append(s)


import nltk
nltk.download()
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
p = sia.polarity_scores('it is a good dog')
p


print(p)
sia = SentimentIntensityAnalizer
sia.polarity_scores("this is a string.")

