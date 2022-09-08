#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:10:57 2022

@author: lfw25
"""

from tkinter import *                 
from tkinter.ttk import *                       # ttk allows styles to be applied to widgets

window = Tk()                                   # Created a root window and initialises Tk's capabilities


h = Scrollbar(window, orient = 'horizontal')
v = Scrollbar(window)
T = Text(window, height = 10, width = 24, wrap = 'none', xscrollcommand = h.set, yscrollcommand = v.set)

h.pack(side = BOTTOM, fill = X)
v.pack(side = RIGHT, fill = Y)

T.insert(INSERT, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \n Suspendisse lorem sem, dapibus \nvenenatis enim a, posuere interdum velit. Phasellus quis turpis enim. \nNullam pharetra urna augue, vel posuere massa interdum a. Maecenas nunc est, dictum at lorem suscipit, imperdiet suscipit lectus. Morbi vehicula magna ac facilisis cursus. Cras imperdiet,\n lectus ut maximus placerat, tellus er\nat aliquam ante, vesti\nbulum mollis neque augue sit amet mi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nulla sit amet mi eget ex cursus bibendum a sit amet augue. Sed hendrerit efficitur viverra. Etiam a mollis lectus. Mauris eget odio risus. Etiam tincidunt libero est, at tempor arcu elementum at. Nunc mauris nulla, bibendum vitae orci eget, vehicula dapibus velit. Aliquam lobortis malesuada scelerisque. Mauris eleifend nibh eu erat pretium, quis efficitur erat aliquam. Cras hendrerit eros vitae nisi vulputate tempus. Duis iaculis, nisl id venenatis volutpat, augue tellus varius nunc, a rutrum dolor diam sit amet neque. Sed et ligula a dolor elementum congue. Praesent dolor eros, eff\nicitur\n sed auctor a, commodo sit amet sapien. Nunc at ligula purus. Aene\nan eget velit id justo venenatis pharetra pulvinar \nfinibus odio. Maecenas suscipit sem at sagittis faucibus. \nPhasellus eu mauris eu risus aliquet rhoncus.")

T.pack(side=TOP, fill = X)
h.config(command = T.xview)
v.config(command = T.yview)

window.mainloop()                               # Initialises the main loop which continually awaits user input on the GUI and allows user events on widgets (like typing)