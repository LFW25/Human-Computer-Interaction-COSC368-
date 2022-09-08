#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:43:40 2022

@author: lfw25
"""

from tkinter import *                 
from tkinter.ttk import *
import tkinter as tk

def clear_data(data):
    '''
    Clicking on the "Clear” button is supposed to make the Label and Entry widgets blank;
    the click will call a function called clear_data, passing in a reference to the StringVar object
    '''
    data.set("")

def to_display(ch):
    data.set(data.get() + ch)


window = Tk()

data = StringVar()
data.set("Default Text")

top_frame = Frame(window)
top_frame.pack(expand = True, fill = 'both', side = 'top')

text_frame = Frame(top_frame)
text_frame.pack(padx = 20, pady = 10, side = 'left')

button_frame = Frame(top_frame)
button_frame.pack(padx = 20, pady = 10, side = 'right')

label = Label(text_frame, textvariable=data)
label.pack(side = 'left')

clear = Button(button_frame, text = "Clear", command = lambda: clear_data(data))
clear.pack(side = 'right')


board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

kb_frame = Frame(window, borderwidth=4, relief=RIDGE)
kb_frame.pack(side="bottom", fill="y", padx=5, pady=5)

for line in board:
    kb_line_frame = Frame(kb_frame)
    kb_line_frame.pack(side = 'top')
    for ch in line:
        b = tk.Button(kb_line_frame, text = ch, width = 1, command = lambda x = ch: to_display(x))
        b.pack(side = 'left')

window.mainloop()