# Write a function called censor that takes two strings, text and word, as input. 
# It should return the text with the word you chose replaced with asterisks.
# The number of asterisks you put should correspond to the number of letters in the censored word.


def censor(text, word):
    words = text.split()
    for i in range(0, len(words)):
        if words[i] == word:
            words[i] = len(word) * "*"
    return " ".join(words)