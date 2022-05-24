#!/usr/bi

#######################
#      Dictionaries
#      Name : Bob Afwata
#      Date : 23/5/2022
######################

#   Initalizing dictionaries
student ={"Name":"Bob","age": 18,"gender":"female","hobby":"drawing"}
print(student["Name"])
print(student["age"])
print(student["gender"])
print(student["hobby"])

#Adding key value pairs 

student["id.No"]="308765"
student["movie"]="hatching"
student["colour"]="blue"
print(student)

#staring with an empty dictionary

student = {}
student["fav-food"]="chiken"
student["home_city"]="Naivasha"
student["fav_place"]="coast"
print(student)

#modify values in the dictionary
student = {"Name":"Kendi"}
print(student)
del student["Name"]
print(student)

