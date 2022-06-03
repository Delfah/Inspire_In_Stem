#! /usr/bin/python

##############################
#functions in python
#name : Kendi
#date :31,may,2022

# block of code which gets executed together
#initializing the functions/defining a funtion
#calling functions

#from tkinter import Y


#def say_hello():
    #print("Hello from JKUAT")
    #x=4
   # y=7
  #  z=x+y
 #   print(z)
#say_hello()

# sound made by animals
#def bark():
 #   print("Dogs bark wooof wooof")
#def meew():
 #   print("cats meew meew meew")
#def crow():
 #   print("cock crows crow crow")
#def moow():
 #   print("cow moow moow moow")
#bark()
#meew()
#crow()
#moow() 

# functions parameters
#def add_numbers(x,y):
  #  sum_nums = x+y
 #   print("The sum of numbers:",sum_nums)
#add_numbers(40,50)
#add_numbers(100,350)
#add_numbers(200,360)
#add_numbers(750,890)    

# product of the numbers
#def prod_numbers(x,y):

  #  prod_numbers = x * Y
 #   print("The product of numbers:",prod_numbers)
#prod_numbers(40,60)
#prod_numbers(4,6)
#prod_numbers(30,20)


# #############
# date 3,june,2022
# default parameters
#################

def print_name(name = "Kendi"):
    print(name)

print_name("James")    

# return from a function

def get_sum(num1,num2):
    sum_nums = num1 + num2
    return sum_nums
print(get_sum(7,12))   

# getting the powers of numbers

def powers (number,power):
    pow_num = number **power
    return pow_num
print (powers(6,4))   

# typing your full name

def get_full_name(f_name,s_name):
    full_name = f_name +" "+  s_name
    return full_name
print( get_full_name("kendi","Delfah"))

# returning a dictionary from a function

def create_full_name(first_name,second_name):
    person = {'first':first_name,'second':second_name}
    return person 
student = create_full_name("kendi","Delfah")
print(student)

#parsing a list in a function

def greet_friends (names):
    for name in names:
        message = "Hello! " + name.title() + "!"
        print(message)
friends = ['Sharon', 'steph' ,'stacy']
greet_friends(friends)   








