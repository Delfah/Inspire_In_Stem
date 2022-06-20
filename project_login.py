from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return
tkWindow = Tk()  
tkWindow.geometry('300x300')  
tkWindow.title("KENDI'S LOGIN PAGE")
tkWindow.config(bg='purple')
usernameLabel = Label(tkWindow, text="Enter User Name",font=("Arial",15)).grid(row=1, column=2)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=2, column=2)  
passwordLabel = Label(tkWindow,text="Enter Password",font=("Arial",15)).grid(row=3, column=2)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=4, column=2)  

validateLogin = partial(validateLogin, username, password)
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=6, column=2)  

tkWindow.mainloop()