x= input("Enter the string: ")
a= input("Enter the charcter to be replaced: ")
b= input("Enter the character to replace " + a + " by: ")
l=len(x)
m=0
while m< l:
    if x[m]==a:
      x=(x[0:m] + b + x[m+1:])
    m=m+1
print (x)