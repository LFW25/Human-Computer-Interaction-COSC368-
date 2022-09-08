#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:36:12 2022

@author: lfw25
"""
###
# Without Lambda
###
'''
from tkinter import *
from tkinter.ttk import * 
def add_one():
    value.set(value.get()+1)

def wow(event):
    label2.config(text="WWWWOOOOWWWW")

window = Tk()
value = IntVar(0)
label = Label(window, textvariable=value)
label.pack()
label2 = Label(window)
label2.pack()
button = Button(window, text="Add one", command=add_one)
button.bind("<Shift-Double-Button-1>", wow)
button.pack()
window.mainloop()
'''

###
# With Lambda
###
'''
from tkinter import *
from tkinter.ttk import * 
def change(the_value, n):
    the_value.set(the_value.get()+n)

window = Tk()
value = IntVar(0)
label = Label(window, textvariable=value)
label.pack()
button = Button(window, text="Left +1, Right -1")
button.bind("<Button-1>", lambda event: change(value, 1))
button.bind("<Button-3>", lambda event: change(value, -1))
button.pack()
window.mainloop()
'''