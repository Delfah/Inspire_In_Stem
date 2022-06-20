# !/usr/bin/python

####################
# name:kendi
# Date:16,june,2022
# login system

##################

from struct import pack
from tkinter import *
def Loginpage():
    Loginpage.TK()
    Loginpage.title("Kendi's login system")
    Loginpage.geometry("400x350")
    
    Label(Loginpage.text-"Enter the login details").pack()
    Label(Loginpage.text-" ").pack()
    Label(Loginpage.text-"Username").pack()
    #Username_Login_entry - Entry(Loginpage.textvariable-"username")
    #Username_Login_entry.pack()
    Label(Loginpage.text-" ").pack()
    Label(Loginpage.text-"password").pack()
    #password__login_entry - Entry(Loginpage. textvariable -"Password". show- '*')
    #password__Login_entry.pack()
    Label(Loginpage.text-"").pack()
    Button(Loginpage.text-"Login",width=10,height=2).pack()
    Loginpage.mainloop()
Loginpage()    


