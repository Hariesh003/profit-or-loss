x=float(input("Enter the price of a dozen mangoes"))
y=float(input("Enter the price at which 1 mango is being sold"))
z=y*12;
if  x<z:
    profit=x-z;
    print("profit:Rs.",profit)
elif  x>z:
    loss=x-z;
    print("loss:Rs.",loss)
else:
    print("no profit nor loss")
    
