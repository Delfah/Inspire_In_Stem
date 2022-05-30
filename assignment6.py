#!usr/bin/python

# checking if a number is divible by 5 or 7


x = int(input("enter number:"))
if (x % 7==0)  or (x % 5==0):
    print(f"the number {x} is divisible by 7 or 5")
else:
    print(f"the number {x} is not divisible by 7 or 5")




