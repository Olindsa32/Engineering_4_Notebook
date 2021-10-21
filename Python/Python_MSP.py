# Python Program 04 - MSP (ENGR4)
#Written by Owen Lindsay
#10.19.2021

word = input("Player 1 pick a word")
print ("\n" * 50)
length = len(word)
emptyString = ("_" * length)
correctGuess = ""
missedGuess = ""

    
def wordLength():
    print (emptyString)
def man(): 
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
while (emptyString != word):
    guess = input("Player 2 guess a letter")
    if (guess in word):
        correctGuess = correctGuess + guess
        print("Your correct guesses are:" + correctGuess)
    else:
        missedGuess = missedGuess + guess
        man()
    for i in range (0, len(word)):
        if ((word[i]) in correctGuess):
            emptyString = emptyString[:i] + word[i] + emptyString [i+1:]
    print(emptyString)
    if(len(correctGuess) == len(emptyString)):
        print("Winner Winner Chicken Dinner!")
        break
    if(len(missedGuess) == 6):
        print("you lose :(")
        break
