# Python Strings and Loops
# Written by Owen Lindsay
# 9/28/21
def splitWords(word):   # Creates a function to split each word into a list of the letters
    return list(word)   # The actual command to split the words; I will use this function later after I split the sentence
sentence = input('Type in your text, then press Enter:')    # Asks a question so that you can respond with a random sentence to work on
for word in sentence.split():   # Splits the sentence into individual words
    for character in splitWords(word):  # this line and the line below are calling the function to split the words then printing each character in a seperate line
        print(character)
    print('-')  # This puts the dash in before repeating the whole thing to print the next word
