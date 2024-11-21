# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:46:59 2024

@author: user
"""

buf = 1
def bufff():
    global buf
    buf *=1.2
    
    
    
def to0():
    global click
    global buf
    click =0
    count_label.config(text=f"點:{click}")
    buf = 1
def onclick(event):
        catlab.config(text = "pop",image=open_mouth_image, compound='center',font=("Ariel",200))
        window.after(200,lambda:catlab.config(image=closed_mouth_image))
        window.after(200,lambda:catlab.config(text=""))
        global click
        click +=buf
        count_label.config(text=f"點:{click}")
        
import tkinter as tk
from PIL import Image,ImageTk

window = tk.Tk()
window.title("pop")
window.geometry("500x500")
window.resizable(False,False)

closed_mouth_image = ImageTk.PhotoImage(Image.open("closed_mouth.jpg").resize((300,300)))
open_mouth_image = ImageTk.PhotoImage(Image.open("open_mouth.jpg").resize((300,300)))

catlab = tk.Label(window,image = closed_mouth_image)
catlab.pack(pady=20)

count_label = tk.Label(window,text = "點:0",font=("Ariel",18))
count_label.pack(pady = 10)
click =0
catlab.bind("<Button-1>",onclick)
reset = tk.Button(window,text="重置",command=to0)
reset.pack()
buff =  tk.Button(window,text="buff",command=bufff)
buff.pack()
window.mainloop()
