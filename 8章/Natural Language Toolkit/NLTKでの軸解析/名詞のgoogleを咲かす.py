from nltk import pos_tag
from nltk import sent_tokenize
from nltk import word_tokenize

sentences = sent_tokenize("Google is one of the best companies in the world. "
                           "I Constantly google myself to see what I'm up to.")
nouns = ["NN", "NNS", "NNP", "NNPS"]

for sentence in sentences:
    if "google" in sentence.lower():
        words = word_tokenize(sentence)
        tagged_words = pos_tag(words)
        for tegged_word in tagged_words:
            word = tegged_word[0]
            word_class = tegged_word[1]
            if word.lower() == "google" and word_class in nouns:
                print(sentence)
