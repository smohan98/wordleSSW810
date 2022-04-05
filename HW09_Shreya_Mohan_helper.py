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
        bad = list(wordle_set - word_set)

        for i in range(len(stmt)):
            if  stmt[i] == '`' or stmt[i] == '"':
                continue
            elif i+1<len(stmt) and (stmt[i+1] == '`' or stmt[i+1] == '"'):
                correct += '_'
            else:
                correct += stmt[i]
        return good , bad , correct

    def possible_words(self,good, bad, correct,prev)->list:
        # good = input("Enter good letters:")
        # if len(good) > 5:
        #     while len(good)>5:
        #         good = input("Enter good letters:")
        # bad = input("Enter bad letters:")
        for letter in bad:
            if letter in good:
                bad = list(filter(lambda i : i not in good, bad))
        # print("The bad letters considered are:")
        # print('"'+''.join(bad)+'"')
        # print(result)  
        # correct = input("Enter letters at correct position(optional). Press enter to skip this step.")

        self.file_wordRank()
        if (good == None or len(good)==0) and (bad == None or len(bad)==0) and (correct == None or len(correct) == 0):
            return self.words[:50]
        else:
            output = []
            for word in self.words:
                if word in prev:
                    continue
                if any(item in word for item in bad):
                    continue
                if not all(elem in word  for elem in good):
                    continue
                # if len(correct)==5:
                f = True
                for idx, letter in enumerate(correct):
                    if letter == '_':
                        continue
                    if word[idx] != letter:
                        f = False
                        break
                if f:
                        output.append(word)
                        # start.next_value = Node(word)
                        # start = start.next_value
                # else:
                    # start.next_value = Node(word)
                    # start = start.next_value
                    # print(word)
                    # output.append(word)
            # output=output.next_value
            # total=1
            # print(output.data)
            # while output:
            #     output = output.next_value
            #     total+=1
            return output
            

f = Helper()
