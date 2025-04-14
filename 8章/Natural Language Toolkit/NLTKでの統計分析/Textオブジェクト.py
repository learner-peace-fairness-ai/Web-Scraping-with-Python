from nltk import Text
from nltk import word_tokenize

tokens = word_tokenize("Here is some not veri interesting text")
text = Text(tokens)

print(text)
