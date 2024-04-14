# import tkinter lib
from tkinter import *

# set the main program root
root = Tk()

# define our button widget
myButton = Button(root, text='Click me', padx=20, pady=10,
                  # we used here a lambda function to run our button command
                  command=lambda: print('hello world'))

# now we gonna use function that declared with def


def myFunction():
    print('hello world 2')


myButton2 = Button(root, text='Click me 2', padx=20,
                   pady=20, command=myFunction)

# set our button on the screen
myButton.pack()
myButton2.pack()


# set our program title
root.title('WE School App')

# set our starting app size
# width x height
root.geometry('400x400')

# run our program
root.mainloop()
