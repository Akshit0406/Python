import random

x= random.random() #Genereates random number
print (x)

xa= random.randint(5,10) # Generates Random Integer between 5 and 10. Both numbers in brackets are inclusive.
print (xa) 

xb=random.randrange(5,8) # Same as randint. Both Numbers in brackets are inclusive.
print (xb)

s=[5,6,7,8,9,10]
xc= print(random.choice(s))

if xa==xb==xc:
    print("Congratulations You Have Won!" )
else: 
    print("Better Luck Next Time")