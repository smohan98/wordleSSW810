from HW06_Shreya_Mohan_utility import write_logs


def user(attempts, prev , all_words):
    try:
        wordle = input(f"Attempt #{7-attempts}\nEnter a 5 letter word \n")
    except Exception as e:
        write_logs(f"ERROR : INPUT ERROR {e}",True) 
    write_logs(f'USER ENTERED: "{wordle.upper()}"')
    if not wordle:
        print("Thank you for playing, exiting game now")
        write_logs(f"USER EXITED THE GAME")
        quit()
    #to convert all input to upper case
    wordle=wordle.upper()
    #to check if the input is not of length 5 and is not consisting of only alphabets
    if len(wordle) != 5 or not wordle.isalpha():
        write_logs(f"ERROR : USER ENTERED AN INVALID WORD",True)
        return False,"Please enter a valid 5 letter word consisting of only alphabets."
    if wordle.lower() not in all_words:        
        # print("Word is not in dictionary")
        write_logs(f"ERROR : USER ENTERED A WORD WHICH IS NOT IN THE DICTIONARY",True)
        return False,"Word is not in dictionary"
    if wordle in prev:        
        # print("You have already entered this word.")
        write_logs(f"ERROR : USER ENTERED A USED WORD",True)
        return False,"You have already entered this word."
    #to check if the input is of length 5 and is consisting of only alphabets
    if len(wordle)==5 and wordle not in prev and wordle.isalpha():
       return True,wordle.upper()

       