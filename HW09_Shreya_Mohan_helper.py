import os
from csv import reader


class Node:
   def __init__(self, data : any = None) -> None:
      self.data = data
      self.next_value = None

class Helper:

    def __init__(self):
        self.words = []

    def file_wordRank(self):
        src_file = 'wordRank.csv'
        src_dir = os.getcwd()
        src_file_location = os.path.join(src_dir, src_file)
        self.words= []
        try:
            with open(src_file_location, 'r') as f:
                r = reader(f)
                # print(r)
                list_of_rows = list(r)
                self.words.append(list_of_rows)
                self.words = [word[1] for word in list_of_rows]
                return self.words
        except Exception as e:
            # self.write_logs(f"ERROR : File Error {e}",True)
            print(e)
            return []

    def good_bad_correct_generate(self,wordle,word,stmt):
        good = []
        bad = []
        correct = ''
        wordle_set = set(wordle)
        word_set = set(word)
        good = list(word_set & wordle_set)
        bad = list(word_set - wordle_set)

        for i in range(len(stmt)):
            if  stmt[i] == '`' or stmt[i] == '"' or (i+1<len(stmt) and (stmt[i+1] == '`' or stmt[i+1] == '"')):
                correct += ' '
            else:
                correct += stmt[i] 

        print(good)
        print(bad)
        print(correct)
        return good , bad , correct

    def possible_words(self,good, bad, correct)->list:
        good = input("Enter good letters:")
        if len(good) > 5:
            while len(good)>5:
                good = input("Enter good letters:")
        bad = input("Enter bad letters:")
        for letter in bad:
            if letter in good:
                bad = list(filter(lambda i : i not in good, bad))
        print("The bad letters considered are:")
        print('"'+''.join(bad)+'"')
        # print(result)  
        correct = input("Enter letters at correct position(optional). Press enter to skip this step.")
        if len(correct)>0:
            while len(correct) > 5:
                print("Please enter exactly 5 items including spaces.")


        if (good == None or len(good)==0) and (bad == None or len(bad)==0) and (correct == None or len(correct) == 0):
            print(self.words[:50])
        else:
            output = start = Node()
            for word in self.words:
                if any(item in word for item in bad):
                    continue
                if any(item not in word for item in good):
                    continue
                if correct != None and len(correct)==5:
                    f = True 
                    for idx, letter in enumerate(correct):
                        if letter == ' ':
                            continue
                        if word[idx] != letter:
                            f = False
                            break
                    if f:
                        start.next_value = Node(word)
                        start = start.next_value
                else:
                    start.next_value = Node(word)
                    start = start.next_value
            output=output.next_value
            total=1
            while output:
                print(output.data)
                output = output.next_value
                total+=1
            print(total-1)
            return output.data
            

f = Helper()
f.file_wordRank()
