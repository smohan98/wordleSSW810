import random
import os

def file_reader():
    path = os.getcwd()+"/words.txt"
    f = open(path, "r")
    data = f.read().splitlines()
    words = []
    for word in data:
        if len(word) == 5:
            words.append(word)
    f.close()
    return words

def word_picker():  
    words = file_reader()
    wordle = random.choice(words)
    return wordle.upper()
