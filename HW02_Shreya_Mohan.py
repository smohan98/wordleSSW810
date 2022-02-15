#***********************************PSEUDOCODE***********************************
#word="SONAR"
# initialize an empty list
# initialize total allowed attempts as 6
# # While number of attempts < 6
#     get word as userinput
#     userinput.upper
#     if word = userinput print correct
#     if userinput length is 5 and userinput not in list and isalpha
#         attempts -1
#         add userinput to list
#         for idx and char in enumerated userinput
#             if char is in word and not in userinput till position i
#                 print char is in word but in/not in right position
#             else print letter is not in userinput
#     elif userinput in list print you have already entered this word.
#     else print please enter a valid 5 letter word consisting of only alphabets 
#*******************************************************************************



print('''WORDLE rules:
> Enter a 5 letter word
> You have to guess the Wordle in maximum tries
> A correct letter turns green
> A correct letter in the wrong place turns yellow
> An incorrect letter turns gray
''')

word="SMORE"
prev=[]
attempts=6

#While loop that works till 6 attempts are made
while attempts:
        wordle = input(f"Attempt #{7-attempts}\nEnter a 5 letter word \n")
        #to convert all input to upper case
        wordle=wordle.upper()
        #if the right word is guessed, the loop is terminated 
        if wordle == word:
            print("Correct word")
            break
        #to check if the input is of length 5 and is consisting of only alphabets
        if len(wordle)==5 and wordle not in prev and wordle.isalpha():
            attempts-=1             #reduces the count after every valid attempt
            prev.append(wordle)     
            stmt=""
        #string comparison and checking the position of each character
            for i,ch in enumerate(wordle):
                if ch in word and ch not in wordle[:i]:
                    stmt += f"The letter {ch} is in the Wordle and "
                    if word[i] == ch:
                        stmt += f"it is in the right position.\n"
                    else:
                        stmt += f"it is not in the right position.\n"
                else:
                    stmt += f"The letter {ch} is not in the Wordle.\n"      
            print(stmt)
        #check for repeated words
        elif wordle in prev:        
            print("You have already entered this word.")
        #validation check
        else:                       
            print("Please enter a valid 5 letter word consisting of only alphabets.")
print("Oops, you are out of chances. Better luck next time!")