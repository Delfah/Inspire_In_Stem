
from tkinter import *
try:
    import tkinter
except:
    import tkinter as Tkinter
import math
import time

class main(tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.x = 150
        self.y = 150
        self.length = 50
        self.creating_all_function_tigger()
    def creating_all_funtions_tigger(self):
        self.create_canvas_for_shapes() 
        self.create_background_()
        self.create_sticks()
        return
    def creating_background_(self):
        self.image = Tkinter.PhotoImage(file ='clock.gif')
        self.canvas.create_image(150,150,image = self.image)
        return
    def create_canvas_for_shapes(self):
        self.canvas = Tkinter.canvas(self,bg ='purple')
        self.canvas.pack(expand = 'yes',fill='both')  
        return
    def creating_sticks(self):
        self.sticks = []
        for i in range (5):
            store = self.canvas.create_line(self.x,self.length.y,self.x+self.length,self.y+self.length,width=4,fill= "green")
        self.sticks.append(store) 
        return

    def update_class(self):
        now = time.localtime()
        t = time.strtime(str(now.tm_hour), "%H")
        hour = int (time.strtime("%I",t))*5
        now = (hour,now.tm_min,now.tm.sec)

        for n,i in enumerate(now):
            x,y = self.canvas.coords(self.sticks[n])[0:2]
            cr =[x,y]
            cr.append(self.length * math.cos(math.radians(i*6)-math.radians(90))+self.x) 
            cr.append(self.length * math.sin(math.radians(i*6)-math.radians(90))+self.y)
            self.canvas.coords(self.sticks[n],tuple(cr))
            return 
            
if __name__ =='_main_':
    root = main()

    while True:
        root.update()
        root.update_idletasks()
        root.update_class()

        


 

          



       
