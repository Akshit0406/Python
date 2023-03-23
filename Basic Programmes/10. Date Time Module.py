import datetime
import random
print(dir(random)) # directory function. Prints all commands in a module.
x= random.randint(1,12)
y= random.randint(1,28)
a= random.randint(0,23)
b= random.randint(0,60)
c= random.randint(0,60) 
z= datetime.datetime(2021,x,y,a,b,c) # We can Generate random dates and times using this method (YYYY-MM-DD hour:minuite:second) 
print (z)
print (z.strftime("%A")) # This generates a random day in the year 2021
print (z.strftime("%B")) # Random Month
print (z.strftime("%w")) # Position of day in the week (Sunday=0, Monday=1, Friday=5...)
print (z.strftime("%d")) # Random day in a month
print (z.strftime("%Y")) # Random Year (Fixed in our case as 2021)
print (z.strftime("%x")) 
print (z.strftime("%X"))
print (z.strftime("%c")) # Day, Date and Time Together