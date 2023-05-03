import nltk 

words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]
stopwords = nltk.corpus.stopwords.words("english")
words = [w for w in words if w.lower() not in stopwords]

print(words)