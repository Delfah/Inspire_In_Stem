# !/usr/bin/python
####################
# name:kendi
# Date:16,june,2022
# login system

##################;

#from struct import pack
from tkinter import *
from typing_extensions import Self
class window(Tk.Toplevel):
    
    def __init__(self,parent):
        super.__init__(parent)
        
        Self.title("Kendi's login system")
        Self.geometry("400x350")
        self.configure(bg = 'purple')
        msg= Label(self,text ="welcome to the loginpage", font = ('Misral 18').place(x=120,y=150))
window = Tk()
window.title("Welcome to kendi's project")
window.configure(bg = 'purple')
window.geometry("400x300")
F_Name = Label(window, text="First Name", font=("Arial ", 20))
S_Name = Label(window, text="Second Name", font=("Arial ", 20))

F_Name.grid(column = 60,row = 100)
S_Name.grid(column = 60,row = 120)

btn = Button(window ,text ="sign up",bg ='green',fg ='black')
btn.grid(column = 100, row = 180)

txt_box = Entry(window, width = 20)
txt_box.grid(column = 100,  row = 100)

txt_box = Entry(window, width = 20)
txt_box.grid(column = 100, row= 120)


window.mainloop()

    
    #Label(Loginpage.text-"Enter the login details").pack()
    #Label(Loginpage.text-" ").pack()
    #Label(Loginpage.text-"Username").pack()
    #Username_Login_entry - Entry(Loginpage.textvariable-"username")
    #Username_Login_entry.pack()
    #Label(Loginpage.text-" ").pack()
    #Label(Loginpage.text-"password").pack()
    #password__login_entry - Entry(Loginpage. textvariable -"Password". show- '*')
    #password__Login_entry.pack()
    #Label(Loginpage.text-"").pack()
    #Button(Loginpage.text-"Login",width=10,height=2).pack()
    #Loginpage.mainloop()
#Loginpage()    


