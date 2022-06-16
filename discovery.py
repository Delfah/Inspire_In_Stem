# !/usr/bin/python

####################
# name:kendi
# Date:16,june,2022
# project

##################
"""""
import hashlib
def signup():
     email = input("Enter email address: ")
     pwd = input("Enter password: ")
     conf_pwd = input("Confirm password: ")
     if conf_pwd == pwd:
         enc = conf_pwd.encode()
         hash1 = hashlib.md5(enc).hexdigest()
     with open("credentials.txt", "w") as f:
         f.write(email + "\n")
         f.write(hash1)
     f.close()
     print("You have registered successfully!")
     else:
         print("Password is not same as above! \n")
#w we will define our second function login( ), which will accept the user’s email and password, hash the entered password and verify it with the password hash stored in the text file along with the email.

#If the entered email and password hash correspond with the one in the text file, then the function will print a success message, and if it doesn’t, it will print a failure message.

def login():
     email = input("Enter email: ")
     pwd = input("Enter password: ")
     auth = pwd.encode()
     auth_hash = hashlib.md5(auth).hexdigest()
     with open("credentials.txt", "r") as f:
         stored_email, stored_pwd = f.read().split("\n")
     f.close()
     if email == stored_email and auth_hash == stored_pwd:
         print("Logged in Successfully!")
     else:
         print("Login failed! \n")
         """
#Now we will combine the two functions and make a menu-driven program with an infinite while loop allowing users to choose to sign up, log in, and exit.

#on exit, the loop will break and will terminate the program.

import hashlib
def signup():
    email = input("Enter email address: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "w") as f:
             f.write(email + "\n")
             f.write(hash1)
        f.close()
        print("You have registered successfully!")
    else:
        print("passsword is not same as above! \n")
def login():
    email = input("Enter email: " )
    pwd = input("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if email == stored_email and auth_hash == stored_pwd:
         print("Logged in Successfully!")
    else:
         print("Login failed! \n")
while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")
#If you like this article, do leave a clap!

28


