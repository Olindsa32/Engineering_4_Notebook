# Engineering_4_Notebook
Engineering 4 Repository for Owen

## Table of Contents
* [Python Dice Roller](#Python_Dice_Roller)
* [Python Calculator](#Python_Calculator)
* [Python Quadratic Solver](#Python_Quadratic_Solver)
* [Python Strings and Loops](#Python_Strings_and_Loops)
---

## Python_Dice_Roller

### Assignment Description

The purpose of this assignment was to create a program that can automatically roll dice. The program also took user input to decide whether another dice should be rolled, or if the program should exit. The spicy version added complexity by asking the user to specify the number of sides on the dice and the number of dice to be rolled at a time. The user was then asked whether they wanted to roll again with the same settings, change the settings, or exit the program. 

### Evidence 

Vanilla version:

![Screenshot 2021-09-10 3 15 26 PM](https://user-images.githubusercontent.com/89222808/133513775-a3eafb43-f836-4e4f-8aa6-e28ca584901f.png)

Spicy version:

![Screenshot 2021-09-10 3 18 38 PM](https://user-images.githubusercontent.com/89222808/133513750-727cdb6c-1c27-4c8a-83d4-50ea9136a221.png)

### Reflection

This assignment was relatively simple, but was challenging because I had not coded in Python for several months. I learned that I could import parts of toolboxes without importing the entire thing, but that changes the syntax of how I call the function later. I also learned about using a while loop to control whether a user wants to exit the program. For the spicy version, I needed to use nested loops. Python determines what is inside a loop by the indent level of each line of text, rather than brackets like some other coding styles. That means I need to be really careful with my tabs!

## Python_Calculator

### Assignment Description

This assignment asked us to input two numbers and output the sum, difference, product, quotient, and modulo.

### Evidence

![Python_Calculator](https://user-images.githubusercontent.com/61475474/134040487-b0c4ce63-e29c-4fc6-af72-4e9fc6cc00a9.png)

### Reflection

I did not have a whole lot of trouble on this assignment. I learned some new things on python like the input and return commands that will be useful for the rest of my assignments. The way I did it I wrote each different equation on each line and assigned them all a different number. Then when I went to print I call my equation function and adding the number at the end to signify the type of equation. One thing that gave me trouble at the end was that I had to turn the answer to each one into a string to get them to print, before I did that it was saying that 5+7 was 57 and stuff like that.

## Python_Quadratic_Solver

### Assignment Description

This assignment had me entering the 3 coefficients in a quadratic equation and asked to get back the roots if they were real and to return that the roots were not real if they weren't real. 

### Evidence

![quadsolverworks](https://user-images.githubusercontent.com/61475474/134213587-56010767-b17b-4f9f-a45b-aac79efa167f.png)

### Reflection

I made 3 variables that the user could enter for the three coefficients in the equation, then I had to add a discriminate variable to check for negative or positive. If it was negative I know that the roots would be imaginary so I just had it says no roots and ask if you wanted to go again. If it was positive I would run the rest of the quad formula on the discriminant and show the output and ask to run again. A hard part of this was that to put the two roots in different lines I had to turn them into a list and I learned how to do that.

## Python_Strings_and_Loops

### Assignment Description


### Evidence

![strings+loopsworks](https://user-images.githubusercontent.com/61475474/135492434-1cdadf49-3062-4112-96cb-8b4cdbbe6adb.png)

### Reflection
