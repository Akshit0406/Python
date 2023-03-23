x= input("Enter a word \n")
print (x[0:6])
print (x[7])
print (x[8:])
print (x[-5])
print (x[-7:-1])

y=0
for n in x:
    if n=="l":
     y=y+1
print ("The number of l's in the string is " + str(y))

len= len(x)
m=0
while m<len:
    a=(x[m])
    b=(x[-m-1])
    if a==b:
     m=m+1
    else:
     print("The given word isnt a pallindrome")
     break;
if m== len:
    print("The given word is a pallindrome")