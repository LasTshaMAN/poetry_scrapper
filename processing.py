from collections import Counter

import nltk
from nltk.corpus import stopwords


def text_to_word_count(text):
    text = text.lower()
    words = nltk.word_tokenize(text)
    words = filter_stop_words(words)
    return dict(Counter(words).most_common())


def filter_stop_words(words):
    # Might use custom list of stop-words (e.g. taken from here - https://www.ranks.nl/stopwords)
    stop_words = set(stopwords.words("english"))
    return [word for word in words if word not in stop_words and word.isalpha()]
