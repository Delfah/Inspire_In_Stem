

 
from tkinter import *
class login:
 def main_account_screen():
    
    mainscreen = Tk()   # create a GUI window 
    mainscreen.geometry("300x250") # set the configuration of GUI window 
    mainscreen.title("Account Login") # set the title of GUI window
 
# create a Form label 
Label(text="Choose Login Or Register", bg="blue", width="300", height="2", font=("Calibri", 13)).pack() 
Label(text="").pack() 
 
# create Login Button 
Button(text="Login", height="2", width="30").pack() 
Label(text="").pack() 

#main_account_creen.mainloop()
login() # call the main_account_screen() function
 