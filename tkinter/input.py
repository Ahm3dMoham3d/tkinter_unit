# import tkinter lib
from tkinter import *

# set the main program root
root = Tk()

# define our input widget
myLabel = Label(root, text='this my input label')
myInput = Entry(root, width=60, borderwidth=5)

# set our input on the screen
myLabel.pack()
myInput.pack()


# set our program title
root.title('WE School App')

# set our starting app size
# width x height
root.geometry('400x400')

# run our program
root.mainloop()
