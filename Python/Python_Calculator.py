# Python Calculator
# Written by Owen Lindsay
# 9/14/21
a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
def equation(a,b,Type):
    # this is my function to get each answer out of the two numbers a and b
    if Type == 1:
        return (a + b)
        # 1 stands for the addition in the Type part of equation
    if Type == 2:
        return (a - b)
        # 2 stands for the subtraction in the Type part of equation
    if Type == 3:
        return (a * b)
        # 3 stands for the multiplication in the Type part of equation
    if Type == 4:
        return round((a / b),2)
        # 4 stands for the division in the Type part of equation
    if Type == 5:
        return (a % b)
        # 5 stands for the remainder in the Type part of equation
print("Sum:\t\t" + str(equation(a,b,1)))
print("Difference:\t" + str(equation(a,b,2)))
print("Product:\t" + str(equation(a,b,3)))
print("Quotient:\t" + str(equation(a,b,4)))
print("Modulo:\t\t" + str(equation(a,b,5)))
# These 5 commands printed the 5 answers and the str makes it a string so it will write out properly
