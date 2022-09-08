from tkinter import *                 
from tkinter.ttk import *                       # ttk allows styles to be applied to widgets

def clear_data(data):
    '''
    Clicking on the "Clear” button is supposed to make the Label and Entry widgets blank;
    the click will call a function called clear_data, passing in a reference to the StringVar object
    '''
    data.set("")


window = Tk()                                   # Created a root window and initialises Tk's capabilities
data = StringVar()                              # Line 4 creates a StringVar, which is a special Tk class supporting mutable strings;
data.set("Data to display")                     # and line 5 sets the value of the string.
label = Label(window, textvariable=data)        # Created a label widget that is a child of the root window. Label displays test stored in "data"
label.grid(row=0, column=0)                     # Uses a grid for geometry management, assigns the widget into the smallest space possible in the first row and column
entry = Entry(window, textvariable=data)        # Creates an entry widget to enter text, controls the content of the data variable
entry.grid(row=1, column=0)                     # Packs the entry widget into the parent window

clear = Button(window, text = "Clear", command = lambda: clear_data(data))
clear.grid(row = 2, column = 0)

s = Style()
s.configure('TButton', font = 'helvetica 24', foreground = 'green')

quit = Button(window, text = "Quit", command = window.destroy)
quit.grid(row = 3, column = 0)

window.mainloop()                               # Initialises the main loop which continually awaits user input on the GUI and allows user events on widgets (like typing)