from tkinter import *
from tkinter.ttk import *
import random
import csv
import time

CANVWD = 1024
CANVHT = 1024
CLICKS_PER_LOCATION = 2


CPL_ITERATOR = 0
LOCATIONS_ITERATOR = 0

USERNAME = "Lily"

prevTime = time.time()

def cartesianProduct(x, y):
    cpArray = []
    for xEl in x:
        for yEl in y:
            cpArray.append((xEl, yEl))
    return cpArray


def log(distance, width, selectionNumber):
    # log the clicks
    # [name] [distance] [width] [selection number] [time]
    
    global USERNAME
    global prevTime
    timeDiff = (time.time() - prevTime) * 1000
    prevTime = time.time()
    
    textFile = "FitsLogbook.csv"
    
    with open(textFile, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([
            USERNAME,
            distance,
            width,
            selectionNumber,
            timeDiff
            ])

def swapBox(left):
    global rectClick
    global rectNoClick
    global LOCATIONS_ITERATOR
    global coordArray
    
    if left == True: # clickRectangle is on the left
        c.coords(rectClick, coordArray[LOCATIONS_ITERATOR][1]) # Switch click to the right
        c.coords(rectNoClick, coordArray[LOCATIONS_ITERATOR][0]) # Switch NoClick to the left
            
            
    else: # clickRectangle is on the right
        c.coords(rectClick, coordArray[LOCATIONS_ITERATOR][0]) # switch click to the left
        c.coords(rectNoClick, coordArray[LOCATIONS_ITERATOR][1]) # switch click to the right

def onClick(event):
    global CLICKS_PER_LOCATION
    global CPL_ITERATOR
    global LOCATIONS_ITERATOR
    global rectClick
    global rectNoClick
    global dwArray
    global coordArray

    if CPL_ITERATOR <= CLICKS_PER_LOCATION:
        # Swap Boxes
        if CPL_ITERATOR % 2 == 0:
            swapBox(True)
        else:
            swapBox(False)

        CPL_ITERATOR += 1
    else:
        # Log clicks
        log(dwArray[LOCATIONS_ITERATOR][0], dwArray[LOCATIONS_ITERATOR][1], LOCATIONS_ITERATOR)
        
        if LOCATIONS_ITERATOR < len(coordArray) - 1:
            CPL_ITERATOR = 0
            # Change positions
            LOCATIONS_ITERATOR += 1
            swapBox(False)
        else:
            # End Tests
            quit()
    

distArray = [64, 128, 256, 512]
widthArray = [8, 16, 32]

dwArray = cartesianProduct(distArray, widthArray)
random.shuffle(dwArray)
coordArray = []

for tup in dwArray:
    distance, width = tup[0], tup[1]
    totSpan = distance + width
    margin = (CANVWD - totSpan)/2
    
    leftBoxCoords = (margin, 0, margin + width, CANVHT)
    rightBoxCoords = (margin + distance, 0, margin + width + distance, CANVHT)
    
    coordArray.append((leftBoxCoords, rightBoxCoords))

window = Tk()

c = Canvas(window, width = CANVWD, height = CANVHT)
c.pack()

rectClick = c.create_rectangle(coordArray[0][0], fill="green")
rectNoClick = c.create_rectangle(coordArray[0][1], fill="blue")

c.tag_bind(rectClick, "<Button-1>", onClick)


window.mainloop()