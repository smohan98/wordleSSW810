import random
import os

# from HW06_Shreya_Mohan_utility import Utility, file_transfer
import HW06_Shreya_Mohan_utility as util

class Dictionary:

    def __init__(self):
        self.words = []
        self.utils = util.Utility()

    def __str__(self):
        return f'Dictionary: ({self.words}, {self.utils})'

    def file_reader(self):
        self.words.clear()
        path = os.getcwd()+"/words.txt"
        f = open(path, "r")
        data = f.read().splitlines()
        # words = []
        for word in data:
            if len(word) == 5:
                self.words.append(word)
        f.close()
        return self.words

    def word_picker(self,used_words):  
        try:
            words = self.utils.file_transfer()
            wordle = random.choice(words)
            while wordle.upper() in used_words:
                wordle = random.choice(words)
            return wordle.upper()
        except Exception as e:
            print(f"Error: {e}")


