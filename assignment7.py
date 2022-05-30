#!/usr/bin/python

# creating a program with numbers in reverse

number = 36789
reversed_number = 0

while number != 0 :
 digit = number % 10
 reversed_number = reversed_number * 10 + digit
 number //= 10

print("The reversed number is:" +str(reversed_number))
