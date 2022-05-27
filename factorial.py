
number = int(input("enter the number"))
factorial = 1
if (number) < 0:
    print("factorial numbers does not exist")
elif (number) == 1:
    print ("factorial of 0 = 1")
else:
    for i in range(1,number + 1):
        factorial = factorial * i
print("factorial of number:",factorial)       
   