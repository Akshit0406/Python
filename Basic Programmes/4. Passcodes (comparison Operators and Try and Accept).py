a=input("enter Username \n")
x=input("enter the first digit of the password \n")

try:
    n= int(x)

except:
    b=input("Please enter a valid number \n")
    n=int(b)
 
y=input("enter the second digit of the password \n")
try:
    m= int(y)       

except:
   c=input("Please enter a valid number \n")
   m= int(c)
 
if (n==4 and m==7):
    print("Welcome "+ a)
else:
    print("Incorrect Passcode")