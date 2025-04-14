import pprint

from nltk import FreqDist
from nltk.book import text6

fdist = FreqDist(text6)
pprint.pprint(fdist.most_common(10))

print(fdist["Grail"])
