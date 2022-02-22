def user(attempts, prev , all_words):
    wordle = input(f"Attempt #{7-attempts}\nEnter a 5 letter word \n")
    if not wordle:
        print("Thank you for playing, exiting game now")
        quit()
    #to convert all input to upper case
    wordle=wordle.upper()
    #to check if the input is not of length 5 and is not consisting of only alphabets
    if len(wordle) != 5 or not wordle.isalpha():
        return False,"Please enter a valid 5 letter word consisting of only alphabets."
    if wordle.lower() not in all_words:        
        # print("Word is not in dictionary")
        return False,"Word is not in dictionary"
    if wordle in prev:        
        # print("You have already entered this word.")
        return False,"You have already entered this word."
    #to check if the input is of length 5 and is consisting of only alphabets
    if len(wordle)==5 and wordle not in prev and wordle.isalpha():
       return True,wordle.upper()

       