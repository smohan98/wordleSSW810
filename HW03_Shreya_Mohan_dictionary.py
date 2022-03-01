import random
import os

from HW06_Shreya_Mohan_utility import file_transfer

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

def word_picker(used_words):  
    try:
        words = file_transfer()
        wordle = random.choice(words)
        while wordle.upper() in used_words:
            wordle = random.choice(words)
        return wordle.upper()
    except Exception as e:
        print(f"Error: {e}")

