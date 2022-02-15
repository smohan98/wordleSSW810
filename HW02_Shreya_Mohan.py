import HW03_Shreya_Mohan_ui as ui
import HW03_Shreya_Mohan_dictionary as dictionary


def letter_checker(stmt,wordle,word):
    for i,ch in enumerate(wordle):
        if ch in word and ch not in wordle[:i]:
            if word[i] == ch:
                stmt += f"{ch}"
            else:
                stmt += f"{ch}`"
        else:
            stmt += f'{ch}"'    
    return stmt


def wordle_checker():
    print('''WORDLE rules:
    > Enter a 5 letter word
    > You have to guess the Wordle in maximum tries
    > A correct letter turns green
    > A correct letter in the wrong place turns yellow
    > An incorrect letter turns gray
    ''')

    prev=[]
    attempts=6
    word = dictionary.word_picker()
    all_words = dictionary.file_reader()


    #While loop that works till 6 attempts are made
    while attempts:
        check,wordle = ui.user(attempts,prev,all_words)

        if check and word == wordle:
            print("Correct Word")
            return
        elif check and word != wordle:
            #reduces the count after every valid attempt
            attempts-=1             
            prev.append(wordle)     
            stmt=""
            #string comparison and checking the position of each character
            stmt = letter_checker(stmt,wordle,word)
            print(stmt)
        else:                       
            print(wordle)
    
    print("Oops, you are out of chances. Better luck next time!")

if __name__ == "__main__":
    while True:
        wordle_checker()
