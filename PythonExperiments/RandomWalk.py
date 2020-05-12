# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:05:04 2020

@author: cteq.eu
"""

# library for visualisation
import tkinter as tkinter
from random import seed
from random import randint


seed(1)

class Walker():
    x=0
    y=0
    width=0
    heigth = 0
    def __init__(self,parent,width,height):
        self.parent=parent
        self.x = width/2
        self.y=height/2
        tkinter.canvas.create_oval(self.x,self.y,self.x,self.y,width=0,fill='black')
    def render(self,x,y):
    #stroke(0)
        #point(x,y)
        #global x,y
        tkinter.canvas.create_oval(x,y,x,y,width=0,fill='black')
    def step(self,x,y,width,heigth):
        #global x,y,width,heigth
        choice = randint(0,4)
        
        if choice == 0:
          x+=1
        elif choice == 1:
          x-=1
        elif choice == 2:
          y+=1
        else:
          y-=1
    
        if x < 0:
            x=0
        if x > width:
            x=width-1
        if y < 0:
            y=0
        if y>heigth:
            y = heigth-1
            

class App:
    def __init__(self, master):
        self.master = master
        Walk = Walker(self.master, 640, 360)

root = tkinter()
app = App(root)
root.title('Random Walker by cteq.eu')
root.mainloop()      