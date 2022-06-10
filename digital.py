# !/usr/bin/python

####################
# name:kendi
# Date:10,june,2022
# digital clock

##################


import sys #to import system files
from tkinter import *   #whole module is imported
import time #importing local time

#Used to display time on the label
def DClock():
    curr_time= time.strftime("%H:%M:%S")
    clock.config(text=curr_time)
    clock.after(100,DClock)

#making window
window=Tk()
window.title('my clock') #adding title to the window

#giving name to our digital clock and styling it
message= Label(window, font=("arial",50), text="kendi's digital clock", fg="green")
message.grid(row=0,column=0)
clock= Label(window, font=("times",100,"bold"),fg="purple")
clock.grid(row=2,column=2)
DClock()
mainloop() #loop is closed