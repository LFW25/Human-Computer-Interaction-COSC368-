#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 13:14:26 2022

@author: lfw25
"""

from tkinter import *                 
from tkinter.ttk import *
import time
import random
import csv

def clear_data(data):
    '''
    Clicking on the "Clear” button is supposed to make the Label and Entry widgets blank;
    the click will call a function called clear_data, passing in a reference to the StringVar object
    '''
    data.set("")

window = Tk()

data = StringVar()

with open('timedTests.csv', 'w', newline='') as csvfile:
    timedTests = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

targetLetters = "abcdef"
letterIndex = 0
numReps = 2
iteratorCount = 1
data.set(targetLetters[letterIndex])


def to_display(b):
    global letterIndex
    global targetLetters
    global numReps
    global iteratorCount    
    
    start = time.time()
    
    if letterIndex >= len(targetLetters) - 1:
        numReps -= 1
        letterIndex = 0
        targetLetters = ''.join(random.sample(targetLetters,len(targetLetters)))
        #print(targetLetters)
    
    elif data.get() == b['text']:
        
        total_time = (time.time() - start) * 1000
        with open('timedTests.csv', 'w', newline='') as csvfile:
            tTWriter = csv.writer(csvfile)
            tTWriter.writerow(["aaggag static {} {} \n".format(iteratorCount, total_time)])
            
            #timedTests = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
            #timedTests.writerow(["balls static {} {} \n".format(iteratorCount, total_time)])
            
            csvfile.close()
        #print("Lily static {} {}\n".format(iteratorCount, total_time))
        
        letterIndex += 1
        data.set(targetLetters[letterIndex])
        iteratorCount = 0
    
        
    if numReps <= 0:
        data.set("Game complete! Well done.")

    iteratorCount += 1
    
        
        


top_frame = Frame(window)
top_frame.pack(expand = True, fill = 'both', side = 'top')

### Text Display Only

display_text_frame = Frame(top_frame)
display_text_frame.pack(padx = 20, pady = 10, side = 'top')

display_text = Label(display_text_frame, textvariable=data)
display_text.pack(side = 'top')

### Clear Button + Text Display

#display_text_frame = Frame(top_frame)
#display_text_frame.pack(padx = 20, pady = 10, side = 'left')

#display_text = Label(display_text_frame, textvariable=data)
#display_text.pack(side = 'left')

#button_frame = Frame(top_frame)
#button_frame.pack(padx = 20, pady = 10, side = 'right')

#clear = Button(button_frame, text = "Clear", command = lambda: clear_data(data))
#clear.pack(side = 'right')

pixel = tk.PhotoImage(width=1, height=1)

board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']


kb_frame = Frame(window, borderwidth = 4, relief = GROOVE)
kb_frame.pack(side="bottom", fill="y", padx=5, pady=5)

for line in board:
    kb_line_frame = Frame(kb_frame)
    kb_line_frame.pack(side = 'top')
    for ch in line:
        b = tk.Button(kb_line_frame, text = ch, image=pixel, width=100, height=100, compound="c")
        b["command"] = (lambda x = b: to_display(x))
        b.pack(side = 'left')
        #b.bind("<Button-1>", lambda _, c = ch: to_display(c.get()))


window.mainloop()