import re

def tokenize_sentence(sentence):
    """Einfache Tokenisierung: Satz in Wörter zerlegen."""
    return re.findall(r'\b\w+\b', sentence.lower())

def bag_of_words(tokenized_sentence, words):
    """Dummy-Funktion für Bag-of-Words (hier nicht verwendet)."""
    return [1 if word in tokenized_sentence else 0 for word in words]
