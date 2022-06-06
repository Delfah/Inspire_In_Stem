# !/usr/bin/python

####################
# name:kendi
# Date:6,june,2022
# operations

##################





def mult_number(x,y):
    result = str(x * y)
    return result

def div_number(x,y):
    result = str(x / y)
    return result

def add_number(x,y):
    result = str(x + y)
    return result

def sub_number(x,y):
    result = str(x - y)
    return result    

class student:
    def __init__(self,name,hobby,year_of_birth): 
        self.name = name
        self.hobby = hobby
        self.year_of_birth = year_of_birth

    def great_student(name):
        print("Hello from" +name.title())           


