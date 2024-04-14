# import tkinter lib
from tkinter import *

# set the main program root
root = Tk()

# define our widgets
myLabel1 = Label(root, text='Hello world 1')
myLabel2 = Label(root, text='Hello world 2')

# set our widgets in the grid system
myLabel1.grid(column=0, row=0)
myLabel2.grid(column=0, row=1)

# set our program title and size
root.title('Grid System')

# set our starting app size
# width x height
root.geometry('400x400')

# run our program
root.mainloop()
