# Python Program 04 - MSP (ENGR4)
#Written by Owen Lindsay
#10.19.2021

word = input("Player 1 pick a word") # asks the first player to pick a word to be guessed
print ("\n" * 50) # clears the screen
length = len(word) # defines the variable length using the command len of variable word from line 5
emptyString = ("_" * length) # creates a variable for the empty string that will be printed for the guesser and defines it as a underscore for each letter of the variable length
correctGuess = "" # sets the variable for correctGuess to be changed later
missedGuess = "" # sets the variable for missedGuess to be changed later

    
def wordLength(): # creates a function that prints the empty string variable
    print (emptyString)
def man(): # creates a function that correlates amount of missed guesses to how many body parts of the hangman are printed
    if (len(missedGuess) >= 1):
        print("_______")
        print("      |")
        print("      O")
    if (len(missedGuess) == 2):
        print("      |")
    elif (len(missedGuess) == 3):
        print("      |--  ")
    elif (len(missedGuess) >= 4):
        print("    --|--  ")
    if (len(missedGuess) == 5):
        print("      \ ")
    elif (len(missedGuess) >= 6):
        print("     /\ ")
while (emptyString != word): # says that if the empty string that slowly gets filled up with letters doesn't equal the word to ask player 2 to guess
    guess = input("Player 2 guess a letter")
    if (guess in word): # says that if the guess is in the word to add it to correctGuess which will just become a bank of letters
        correctGuess = correctGuess + guess
        print("Your correct guesses are:" + correctGuess) # prints all the correct guesses
    else: # says that if guess isn't in the word to add it to the missed guess bank and call the man function from line 15
        missedGuess = missedGuess + guess
        man()
    for i in range (0, len(word)): # asks if i is anywhere from 0 to the end of the word
        if ((word[i]) in correctGuess): # if it is then it will look for it in the correctGuess bank
            emptyString = emptyString[:i] + word[i] + emptyString [i+1:] # this will add the letter into emptyString and change the value of emptyString.
    print(emptyString) # then this prints the progress you have made on the word
    if(len(correctGuess) == len(emptyString)): # if correctGuess equals the emptyString you have been filling then you win
        print("Winner Winner Chicken Dinner!")
        break # ends the program
    if(len(missedGuess) == 6): # if missed guesses hits 6 you lose
        print("you lose :(")
        break # ends the program
