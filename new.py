import random 
#here we will make a project which makes the user guess the word
#we will use the library random in order to choose between a set of words

name = input("what is your name? ")
print("hello there",  name)
print("lets play a game")
#here the progam asks the user for his name 

words = ("angry", "portal","computer", "banana", "orange", "asshole", "bitch", "whore")
#create a tuple of words for the program to chose from 

word = random.choice(words)

print("guess the characters :")
guesses = ''

turns = 12 
#any number of turns can be given to the user

while turns > 0:

    failed =  0
    #counts the number of times the user failed

    for char in word:
        #for all the characters from the input

        if char in guesses:
            print(char)
            #prints the char if it matches the user input

        else:
            print("_")

            failed += 1
            #for every failure, 1 will be implemented

    if failed == 0:
        print("you win, Man")
        #user will win the game if the failed is 0 

        print("the correct word is", word)
        #the correct word will be displayed 

        break
    
    guess = input("enter the character: ")
    #if the user inputs the wrong alphabet then, the program will ask the user to enter another character

    guesses += guess
    #every input character will be stored in guesses

    if guess not in word:

        turns -= 1 
        print("wrong")
        #if the character doesnt match the word, then wrong will be printed

        print("you have", + turns, "turns left")

    if turns == 0:
        print("you loose")

    





