L1= [ "Bananas", " Apples", "Oranges"]
Amt= [5, 5, 10]
Cost= [ 20, 200, 80]

for (L1, Amt, Cost ) in zip(L1, Amt, Cost):
    print("I bought " + str(Amt) + " " + L1 + " at Rupees " + str(Cost) + " each")