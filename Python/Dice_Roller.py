# Automatic Dice Roller
# Written by Owen
# 9/13/21
from random import randint
print("Automatic Dice Roller")
def dice_roller():
    question = input("Press Enter to roll")
    if question == '':
        print("The number is", randint(1,6))
reroll = ""
while reroll == "":
    dice_roller()
    reroll = input("Reroll with Enter or leave with X")
print("Thanks for playing!")
