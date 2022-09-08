#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:06:44 2022

@author: lfw25
"""
###
# Packer
###
'''
from tkinter import *
from tkinter.ttk import * 
window = Tk()
side_labels = ["bottom1", "bottom2", "top1", "top2", "left1", "right1"]
for theside in side_labels:
    button = Button(window, text=theside)
    button.pack(side=theside[0:-1])
window.mainloop()
'''

###
# Gridder 1
###
'''
from tkinter import *
from tkinter.ttk import * 
window = Tk()
for label_num in range(6):
    button = Button(window, text="Button"+str(label_num))
    button.grid(row=label_num // 3, column=label_num % 3)
window.mainloop()
'''

###
# Gridder 2
###
'''
from tkinter import *
from tkinter.ttk import * 
window = Tk()
for label_num in range(6):
    button = Button(window, text="Button" + str(label_num))
    button.grid(row=label_num // 2, column=label_num % 3)
    if label_num==1:
        button.grid(columnspan=2, sticky="ew")
    elif label_num==3:
        button.grid(rowspan=2, sticky="ns")
window.columnconfigure(1, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.mainloop()
'''

###
# Frames
###
from tkinter import *
from tkinter.ttk import * 
window = Tk()
frame_left = Frame(window, borderwidth=4, relief=RIDGE)
frame_left.pack(side="left", fill="y", padx=5, pady=5)
frame_right = Frame(window)
frame_right.pack(side="right")

button1 = Button(frame_left, text="Button 1")
button1.pack(side="top")
button2 = Button(frame_left, text="Button 2")
button2.pack(side="bottom")

for label_num in range(4):
    button = Button(frame_right, text="Button" + str(label_num + 3))
    button.grid(row=label_num // 2, column=label_num % 2)
window.mainloop()