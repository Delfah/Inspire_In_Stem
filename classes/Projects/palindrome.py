#! usr/bin/python

#################
# name:kendi
# date:8,june,2022
# palindromes

#################

# using words


def ispalindrome(s):
    return s == s[::-1]
s = 'reader'
ans = ispalindrome
if ans:
    print("yes")
else:
    print("No")   

# using numbers    

string=input(("Enter a string:"))
if(string==string[::-1]):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")    
