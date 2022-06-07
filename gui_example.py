# !/usr/bin/python

####################
# name:kendi
# Date:7,june,2022
# gui_examples using ktinter

##################

from tkinter import *

def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("pop up window")
    top.configure(bg='grey')
    msg= Label(top,text ="welcome to pop up", font = ('Misral 18').place(x=150,y=150))
    
window = Tk()
window.title("Welcome to my App")
window.configure(bg = 'purple')
window.geometry("400x400")
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



