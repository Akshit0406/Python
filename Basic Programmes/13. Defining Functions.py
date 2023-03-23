def printTwice(): 
    print ("Hello")
    print ("Hello") # we have created a new function called printTwice and defined what does
printTwice()

import math
x= int(input("Enter the number to Raise To Fourth Power \n"))

def FourthPower (x):
    x=math.pow(x,4)
    print ("The Fourth Power is "+ str(x))
    return x
FourthPower(x)