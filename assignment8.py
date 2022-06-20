
from tkinter import *
for PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import*

class clock:
    def __init__(self,root):
        self.root=root
        self.root.title("Gui analog clock")
        self.root.geometry("500x500")
        self.root.configure(bg='purple')

        title=Label(self.root,text="An analog clock",font=('times new roman',50,'bold')).place(x=2,y=40,relwidth=1)
        self.lbl=Label(self.root,bg="green",bg=,relief=RIASED)
        self.lbl.place(x=350,y=150,height=400,width=400)
    def clock_image(self):
        clock=Image.new("RGB",(350,350),(250,250,250))  
        draw=ImageDraw.Draw(clock)
        bg=Image.open("cl.jpg")
        bg=bg.resize(300,300,Image.ANTIALIS) 
        clock.paste(bg,(50,50))
        clock.save("new clock")

        
        

root=Tk()
obj=clock(root)
root.mainloop()
        

          



       
