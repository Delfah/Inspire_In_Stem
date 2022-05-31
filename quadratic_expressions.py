#!/usr/bin/ python

####################
# quadratic in python
# name : Kendi
# date :31,may,2022
###################


import math
a =int(input("enter the coefficient of the first term"))
b =int(input("enter the coefficient of the second term"))
c =int(input("enter the constant"))
w = math.sqrt((b**2)-4*a*c)

def find_roots(a,b,c):
    y1 = ((-b + w)/(2*a))
    y2 = ((-b - w)/(2*a))
    print("The roots of the quadratic equation are:",y1,y2)
find_roots(a,b,c)

# using long metohod 
#def find_roots(a,b,c):
 #   y1 = (-b + math.sqrt((b**2)-4*a*c))/(2*a)
  #  y2 = (+b + math.sqrt((b**2)-4*a*c))/(2*a)
   # print("The roots of the quadratic expression are:"y1,y2)
#find_roots(a,b,c)    



