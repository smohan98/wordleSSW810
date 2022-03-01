import HW03_Shreya_Mohan_ui as ui
import HW03_Shreya_Mohan_dictionary as dictionary
from HW06_Shreya_Mohan_utility import write_logs


def letter_checker(stmt,wordle,word):
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

def wordle_checker(win,guess,used_words):
    print('''WORDLE rules:
    > Enter a 5 letter word
    > You have to guess the Wordle in maximum tries
    > A correct letter turns green
    > A correct letter in the wrong place turns yellow
    > An incorrect letter turns gray
    ''')
    
    prev=[]
    attempts=6

    word = dictionary.word_picker(used_words)
    write_logs(f"RANDOM WORD CHOSEN FOR THE GAME: {word}")
    used_words.append(word)
    all_words = dictionary.file_reader()


    #While loop that works till 6 attempts are made
    while attempts:
        check,wordle = ui.user(attempts,prev,all_words)

        if check and word.strip() == wordle.strip():
            win+=1
            guess[6-attempts] += 1
            write_logs(f"USER ENTERED THE CORRECT WORD: {wordle.upper()}")
            print("Correct Word")
            return win,guess,used_words
        elif check and word != wordle:
            #reduces the count after every valid attempt
            attempts-=1             
            prev.append(wordle)     
            stmt=""
            #string comparison and checking the position of each character
            stmt,count = letter_checker(stmt,wordle,word)
            print(stmt)
        else:                       
            print(wordle)
    
    print("Oops, you are out of chances. Better luck next time!")
    write_logs(f"USER RAN OUT OF CHOICES")
    return win,guess,used_words

def main():
    games_played=0
    win = 0
    guess = [0]*6
    used_words = []
    while True:
        games_played += 1
        win,guess,used_words=wordle_checker(win,guess,used_words)
        print(f"GAMES PLAYED : {str(games_played)}")
        write_logs(f"GAMES PLAYED : {str(games_played)}")
        print(f"WIN PERCENTAGE : {str((win*100)/games_played)}%")
        write_logs(f"WIN PERCENTAGE : {str((win*100)/games_played)}%")
        for i in range(len(guess)):
            print(f"{guess[i]} GAMES WON AT GUESS NUMBER {i+1}")
            write_logs(f"{guess[i]} GAMES WON AT GUESS NUMBER {i+1}")

if __name__ == "__main__":
    main()


