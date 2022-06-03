#! usr/bin/python

#################
# name:kendi
# date:3,june,2022
# passwords

#################


# ask user numbers of passwords they want to generate
# convert num_passwords into integers
# ask user for password length
# convert length password to integers

import random
print('welcome to python generator')

password_length = 5
character = "kendingugi"
for password in range (password_length):
    password = ""
    for c in range(password_length):
        password += random.choice(character)
    print(password) 

       

    
    
