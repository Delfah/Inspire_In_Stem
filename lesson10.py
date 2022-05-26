#!/usr/bin/python
print(range(0,20))
for numbers in range(0,10):
    if(numbers %2==0):
     print(numbers)

# sum of all even numbers between 0 and 50
prod_nums = 1
sum = 0

for numbers in range(0,50):
    if(numbers %2==0):

        sum = numbers + sum
print(sum)

#product of all odd number between 0 and 50


for numbers in range(0,20):
    if (numbers %2 == 1): #odd number
        prod_nums = prod_nums * numbers
print(prod_nums)

#calculating the factorial of 6 and 9


number = 0
while number < 10:
    
    print(number)
    number = number + 1
print (number)

number = 0
while number < 10: 
 if (number%2==0):
    print(number)
 number=number + 1
print (number)





