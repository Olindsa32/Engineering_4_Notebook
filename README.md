# Engineering 4 Notebook
Engineering 4 Repository for Owen

## Table of Contents
* [Python Section](#Python_Section)
* [Onshape Section](#Onshape_Section)
---



# Python_Section
## Table of Contents
* [Python Dice Roller](#Python_Dice_Roller)
* [Python Calculator](#Python_Calculator)
* [Python Quadratic Solver](#Python_Quadratic_Solver)
* [Python Strings and Loops](#Python_Strings_and_Loops)
* [Python Hangman](#Python_MSP)
* [Python Blink](#Python_Blink)
* [Python Shutdown](#Python_Shutdown)
* [Python I2C](#Python_I2C)
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

The reason for this assignment was to learn how to use the split function, arrays, lists, and loops. We wrote a sentence as an input and then seperate each letters with a line break between each letter, and then add a dash in between every word in the sentence and have an extra dash at the end.

### Evidence

![strings+loopsworks](https://user-images.githubusercontent.com/61475474/135492434-1cdadf49-3062-4112-96cb-8b4cdbbe6adb.png)

### Reflection

I had a lot of help on this assignment from other people in the class. I did not understand the concept very well until other people walked me through their code. I had to learn how to use the split function and split the input into each word then call a function that splits all my words.

## Python_MSP

### Assignment Description

This coding assignment makes you use input commands, functions, variables, and arrays. It was used as a test type of assignment to see if we could use all of our coding to do this. We were asked to make a hangman game.

### Evidence

![mspworks](https://user-images.githubusercontent.com/61475474/138313593-fd590a32-f960-4857-b471-52e8db7fcf23.png)

### Reflection

I used a lot of Max Tyree's code on the assignment (mtyree18 on github). I was having trouble understanding a lot of the neccesary parts of the code so I worked through his code with him so he could help me understand each piece of it. It was important to understand areas because the most confusing part of the whole thing was trying to implant the correct guesses into the empty string of ______ that shows how many letters the original word is. The was I did it was by making the empty string equal to empty before the correct guess, then the letter, then the rest of the word that comes afterwards.

## Python_Blink

### Assignment Description

This assignment was the first one done through raspberry pi and made us code it in Python and then send it into github. It had us blink two LEDs. When one is on, the other is off. We also had to print which one was on and off.

### Evidence

https://user-images.githubusercontent.com/61475474/144466595-1a56556b-89f2-47ae-a850-1d13e503636b.mp4

### Wiring

![20211202_115359](https://user-images.githubusercontent.com/61475474/144467345-574618f6-2659-4103-8a1e-2f3fe5cfce0f.jpg)

### Reflection

This assignment was easy to do after I took the starting stuff that was in the canvas assignment and searched up how to use the GPIO assignments. I had two small problems, one of them was that when I added a second LED, I forgot to setup the second output pin at first. The second problem was that I was writing the sleep command as time.sleep instead of just sleep.

## Python_Shutdown

### Assignment Description

This assignment had us shutdown the raspberry pi with a pushbutton and prewritten code. Once we did that we went into a file and added the code to run this program automatically instead of having to call it and then push the button.

### Evidence

https://user-images.githubusercontent.com/61475474/145069841-e73c1d40-a45e-4335-85d6-fb8a26e8e25e.mp4

### Wiring

![20211207_112735](https://user-images.githubusercontent.com/61475474/145068672-e98d6c14-6072-4e41-8bbf-f9406403a8dd.jpg)

### Reflection

This assignment was easy because the code was given to me and the wiring was simple. I struggled a bit because the comments were too long so when I copied the code into raspberry pi it was running into the next line and causing errors. With the wiring I learned how simple a pushbutton is, all it does is when you press down it connects all 4 corners of the button and the wires coming from those corners. This code may be useful going forward if I just keep a button on my breadboard plugged into the same GPIO pin.

## Python_I2C

### Assignment Description

This assignment had us use the accelerometer and display those numbers onto the OLED display.

### Evidence and Wiring

![20220111_114633](https://user-images.githubusercontent.com/61475474/148986123-80f6a45e-4d30-4e17-b474-490328231e81.jpg)

### Reflection

I learned to use the accelerometer and connect it to the OLED display. I struggled with how to change the acceleration numbers to the format we want. I had to divide by 107 to get the numbers looking good. I also had to convert the number to a string and round it to 3 digits.





# Onshape_Section
## Table of Contents
* [Designing a Skateboard](#Onshape_Skateboard)
* [Onshape Legos](#Onshape_Duck_and_Helicopter)
---

## Onshape_Skateboard

### Assignment Description

This Onshape assignment was a guide to building a skateboard, we had to make the deck, baseplate, hangar, bushing, wheel, bearing and insert nuts and bolts. They gave us a guide for each individual step so we could go along and learn how to use new onshape geometry.

### Evidence

![finishedSkateboard](https://user-images.githubusercontent.com/61475474/139104740-f497f141-e4bb-41dc-bb1a-45a2074306ae.png)

### Reflection

This assignment wasn't very hard because everything it was showing me in the guide I already knew. One mistake I made early was making the start of the truck baseplate a part of the deck instead of a new part so when I try to add fillets and stuff with that as the merge scope it didn't work right. But I didn't find that until later because onshape tried to solve it by just merging to other things or filleting different edges. Once I noticed it I had trouble fixing it because when I changed it everything built on top of it was undone because the merge scope was changed to a new part. Once I sorted that out it was smooth sailing.

## Onshape_Duck_and_Helicopter

### Assignment Description

This assignment wanted us to create a lego block and use configurations to essentially create 54 different usable lego blocks after only designing one. Then made you design a simple duck and put it in a drawing and create an instruction booklet to show how to use various features inside the drawings, including BOMs and different POVs. Then we used our created blocks to create our own lego set and instruction booklet

### Evidence

![onshapeDuck](https://user-images.githubusercontent.com/61475474/140966410-5bbb7694-fa55-4c22-8a22-59767af13001.png)
![onshapeHeli](https://user-images.githubusercontent.com/61475474/140966210-96eb8d92-c6da-4ed0-9c94-ae7fc5661ecf.png)

### Reflection

This assignment was supposed to be simple while highlighting how to use configurations and other Onshape features that the guide worked you through. One unique thing I learned was when we moved it down from 2x2 to 1x2. We had to remove the center hole we had been using to lock the other legos in the bottom so we used a configuration, instead of changing the size which is what I knew how to do we just suppressed the whole feature to remove it. When I made my helicopter one thing that made it easier was putting 5 to 10 legos together and copying them so I could paste them together and group them. That was essentially letting me snap 10 pieces together which I had to do a lot across the shell of the helicopter.
