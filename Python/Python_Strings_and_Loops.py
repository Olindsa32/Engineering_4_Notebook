# Python Strings and Loops
# Written by Owen Lindsay
# 9/28/21
def splitWords(word):
    return list(word)
sentence = input('Type in your text, then press Enter:')
for word in sentence.split():
    for character in splitWords(word):
        print(character)
    print('-')
