import random

def file_reader():
    f = open("words.txt", "r")
    data = f.read().splitlines()
    words = []
    for word in data:
        if len(word) == 5:
            words.append(word)
    return words

def word_picker():  
    words = file_reader()
    wordle = random.choice(words)
    return wordle.upper()
