from nltk import ngrams
from nltk import FreqDist
from nltk.book import text6

fourgrams = ngrams(text6, 4)
fourgramsDist = FreqDist(fourgrams)
print(fourgramsDist[("father", "smelt", "of", "elderberries")])
