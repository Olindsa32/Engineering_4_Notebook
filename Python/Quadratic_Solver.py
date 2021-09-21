# Python Qudratic Solver
# Written by Owen Lindsay
# 9/21/21
from math import sqrt
print("Welcome to the Quadratic Solver")
print("Enter the coefficients for ax^2 + bx + c = 0")
# Top 2 lines are printing the greeting to the user before the code starts
def formula(a,b,c):
    d = (b**2) - (4*a*c)
    # This defines the discirminant to check it for being negative or positive
    if d < 0 :
        print("There are no real roots")
        # This is checking d for negative because in the Quadratic Formula you take the square root of the discriminant 
    else:
        Root1 = str((-b-sqrt(d))/(2*a))
        Root2 = str((-b+sqrt(d))/(2*a))
        Roots = [Root1,Root2]
        return Roots
        # This part is for when d is positive it will run the rest of the Quadratic Formula on it and define each one 
        # It defines them as Root 1 and Root 2 so I can plug them into an array called Roots
        # I then return that array so that I can print it at the end
retry = ""
# Defining this as empty makes it so I can hit Enter to rerun the while loop
while retry == "":
    a = int(input("Enter coefficient a:"))
    b = int(input("Enter coefficient b:"))
    c = int(input("Enter coefficient c:"))
    # These three commands are going to ask me the question in the green
    # I am going to be able to answer due to the input portion and the answer will equal a,b,c
    Roots = formula(a,b,c)
    # Defining the thing that got returned from the function as the function from the top to relate them.
    if len(Roots) > 0:
        print(Roots[0])
        print(Roots[1])
        # This if statement is asking how long the roots are so that if there are no roots that doesn't activate and glitch
        #I then print the 1st and 2nd numbers entered in the Roots array with those 2 print lines
    retry = input("Retry with Enter or leave with any button")
    # Asking me if I want to go again, if i type anything in it will kick me out of the while loop and run the print goodbye line
print("Goodbye!")
