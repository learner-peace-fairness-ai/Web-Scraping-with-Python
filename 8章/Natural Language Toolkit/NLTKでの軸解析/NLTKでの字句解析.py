from nltk import pos_tag
from nltk import word_tokenize

text1 = word_tokenize(
    "Strange women lying in ponds distributing swords is nobasis for a system of government. "
    "Supreme executive power derives from a mandatefrom the messes, not from some farcical aquatic ceremony."
)
print(pos_tag(text1), end="\n\n")

text2 = word_tokenize("The dust was thick so he had to dust.")
print(pos_tag(text2))
