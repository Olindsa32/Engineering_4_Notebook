# Engineering_4_Notebook
Engineering 4 Repository for Owen

## Hello Python Assignment
  Automatic Dice Roller

  Written by Owen

  from random import randint

  print("Automatic Dice Roller")

  def dice_roller():

      question = input("Press Enter to roll")
    
     if question == '':
    
          print("The number is", randint(1,6))
        
  dice_roller()
