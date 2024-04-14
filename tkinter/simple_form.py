# import tkinter lib
from tkinter import *

# set the main program root
root = Tk()

# define our function to show input value


def showInputValue():
    valueLabel = Label(root, text=myInput.get())
    valueLabel.pack()


# define our widgets
myLabel = Label(root, text='Input label')
myInput = Entry(root, width=60, borderwidth=5)
myButton = Button(root, text='Print the input value', command=showInputValue)


# set our input on the screen
myLabel.pack()
myInput.pack()
myButton.pack()


# set our program title
root.title('WE School App')

# set our starting app size
# width x height
root.geometry('400x400')

# run our program
root.mainloop()
