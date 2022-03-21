import HW03_Shreya_Mohan_ui as ui
import HW03_Shreya_Mohan_dictionary as dictionary
# from HW06_Shreya_Mohan_utility import write_logs
# from HW07_Shreya_Mohan_statistics import file_statistics,word_ranking
import HW06_Shreya_Mohan_utility as util
import HW07_Shreya_Mohan_statistics as stat

class Game:

    def __init__(self):
        self.words = []
        self.d = dictionary.Dictionary()
        self.utils = util.Utility()
        self.stats = stat.Statistics()
        self.u = ui.Info()

    def __str__(self):
            return f'Game: ({self.d}, {self.utils}, {self.stats}, {self.u})'


    def letter_checker(self,stmt,wordle,word):
        try:
            count = 0
            for i,ch in enumerate(wordle):
                if ch in word and ch not in wordle[:i]:
                    if word[i] == ch:
                        stmt += f"{ch}"
                        count+=1
                    else:
                        stmt += f"{ch}`"
                else:
                    stmt += f'{ch}"'    
            return stmt,count
        except Exception as e:
            print(f"Error: {e}")

    def wordle_checker(self,win,guess,used_words):
        try:
            print('''WORDLE rules:
            > Enter a 5 letter word
            > You have to guess the Wordle in maximum tries
            > A correct letter turns green
            > A correct letter in the wrong place turns yellow
            > An incorrect letter turns gray
            ''')
            
            prev=[]
            attempts=6

            word = self.d.word_picker(used_words)
            self.utils.write_logs(f"RANDOM WORD CHOSEN FOR THE GAME: {word}")
            used_words.append(word)
            all_words = self.d.file_reader()


            #While loop that works till 6 attempts are made
            while attempts:
                check,wordle = self.u.user(attempts,prev,all_words)

                if check and word.strip() == wordle.strip():
                    win+=1
                    guess[6-attempts] += 1
                    self.utils.write_logs(f"USER ENTERED THE CORRECT WORD: {wordle.upper()}")
                    print("Correct Word")
                    return win,guess,used_words
                elif check and word != wordle:
                    #reduces the count after every valid attempt
                    attempts-=1             
                    prev.append(wordle)     
                    stmt=""
                    #string comparison and checking the position of each character
                    stmt,count = self.letter_checker(stmt,wordle,word)
                    print(stmt)
                else:                       
                    print(wordle)
            
            print("Oops, you are out of chances. Better luck next time!")
            self.utils.write_logs(f"USER RAN OUT OF CHOICES")
            return win,guess,used_words
        except Exception as e:
            print(f"Error: {e}")
            
    def main(self):
        try:
            games_played=0
            win = 0
            guess = [0]*6
            used_words = []
            self.stats.file_statistics()
            self.stats.word_ranking()
            while True:
                games_played += 1
                win,guess,used_words=self.wordle_checker(win,guess,used_words)
                print(f"GAMES PLAYED : {str(games_played)}")
                self.utils.write_logs(f"GAMES PLAYED : {str(games_played)}")
                print(f"WIN PERCENTAGE : {str((win*100)/games_played)}%")
                self.utils.write_logs(f"WIN PERCENTAGE : {str((win*100)/games_played)}%")
                for i in range(len(guess)):
                    print(f"{guess[i]} GAMES WON AT GUESS NUMBER {i+1}")
                    self.utils.write_logs(f"{guess[i]} GAMES WON AT GUESS NUMBER {i+1}")
        except Exception as e:
            print(f"There has been an error: {e}")

if __name__ == "__main__":
    g= Game()
    g.main()


