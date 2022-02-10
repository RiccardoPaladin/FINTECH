import nltk
nltk.download('punkt')
text = 'this is an sample.'
tokens = nltk.word_tokenize(text)   #split also the dot at the end and present a list for each element
tokens                              #if the document is long can be done sentence tonkenization adn then do word tokenizarion for each sentence with a loop
text2 = "this isn't a good test"
tokens1 = nltk.word_tokenize(text2)   #split is and n't
tokens1
tag = nltk.pos_tag(tokens)       #it gives for each element of the list which kind of word is, like noun berb or abjective  POS= part of speech
tag   #JJ= objective   VB=verb VBD= past verb  (look at pos labels list)


from nltk.util import ngrams

n_grams = ngrams(tokens, 3 )
n_grams       #group the sentence slitted in list in groups of 3 words

from nltk.stem.porter import *
stemmer = PorterStemmer()
stemmer.stem("jumps")     #it gives the stem of the word (jump) so the base form

from nltk.stem import WordNetLemmatizer
lemmatizer= WordNetLemmatizer()    #decognugate vrebs, from past to infinite
lemmatizer.lemmatize('was')       #it should give be


from vaderSentiment.vaderSentiment import SentimentIntensityAnalizer
sia = SentimentIntensityAnalizer
sia.polarity_scores("this is a string.")   #it gives a dictionary with positive, negative compound words based on the sense of the phrase. it gives the percentage of positivity and negativity
#it recognize the meaning or the words and also things like esclamation points
#when we change the sententence look at the compound
#it recognize also smile :)
#it didn't work thta much because cannot get the sarcasm and intonations
#it can be used on influence people and create a bot to invest on stocks that are mentioned by very influence people


