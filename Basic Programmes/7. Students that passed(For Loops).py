a= int(input("enter pass marks out of 100 \n"))
passers=0
x= [87, 89, 34, 52, 67, 53, 1, 3, 6, 45, 87, 49, 90]
for n in x:
    y= int (n)
    if y>= a:
     passers= passers+ 1
print("The number of students that passed is " + str(passers))