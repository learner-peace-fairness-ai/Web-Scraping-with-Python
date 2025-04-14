from nltk import bigrams
from nltk import FreqDist
from nltk.book import text6

bigrams = bigrams(text6)
bigramsDist = FreqDist(bigrams)
print(bigramsDist[("Sir", "Robin")])
