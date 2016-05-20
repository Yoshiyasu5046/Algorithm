# The function "anti_vowel" takes a string input and returns text without vowels


vowels = ["a", "i", "u", "e", "o","A", "I", "U", "E", "O"]

def anti_vowel(text):
    if type(text) is not str:
        text = str(text)
    result = []
    for c in text:
        if c not in vowels:
            result.append(c)
    return "".join(result)
        