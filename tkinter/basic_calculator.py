# import tkinter lib
from tkinter import *

# set the main program root
root = Tk()


# define our functions


def insertFunc(e):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(e))


def clear_one():
    entry.delete(len(entry.get()) - 1, END)


# constants
first_num = 0
second_num = 0
operator = '+'


def clear():
    global operator
    global first_num
    global second_num

    first_num = 0
    second_num = 0
    operator = '+'
    entry.delete(0, END)


def operatorFunc(e):
    global operator
    global first_num
    operator = e
    first_num = float(entry.get())
    buttonEqual['state'] = 'normal'

    entry.delete(0, END)


def equal():
    second_num = float(entry.get())
    value = 0
    if (operator == '+'):
        value = (first_num + second_num)
    elif (operator == '-'):
        value = (first_num - second_num)
    elif (operator == '*'):
        value = (first_num * second_num)
    elif (operator == '/'):
        value = (first_num / second_num)
    elif (operator == '%'):
        value = (first_num % second_num)
    entry.delete(0, END)
    entry.insert(0, str(value))


# define our widgets
entry = Entry(root, width=50, borderwidth=5)

# define our buttons

# first row
rest = Button(root, text='%', padx=20, pady=20,
              command=lambda: operatorFunc('%'))
multiply = Button(root, text='x', padx=20, pady=20,
                  command=lambda: operatorFunc('*'))
divide = Button(root, text='/', padx=20, pady=20,
                command=lambda: operatorFunc('/'))
delete = Button(root, text='delete', padx=20,
                pady=20, command=lambda: clear_one())

# second row
button7 = Button(root, text='7', padx=20, pady=20,
                 command=lambda: insertFunc(7))
button8 = Button(root, text='8', padx=20, pady=20,
                 command=lambda: insertFunc(8))
button9 = Button(root, text='9', padx=20, pady=20,
                 command=lambda: insertFunc(9))
minus = Button(root, text='-', padx=20, pady=20,
               command=lambda: operatorFunc('-'))

# third row
button4 = Button(root, text='4', padx=20, pady=20,
                 command=lambda: insertFunc(4))
button5 = Button(root, text='5', padx=20, pady=20,
                 command=lambda: insertFunc(5))
button6 = Button(root, text='6', padx=20, pady=20,
                 command=lambda: insertFunc(6))
plus = Button(root, text='+', padx=20, pady=20,
              command=lambda: operatorFunc('+'))

# forth row
button1 = Button(root, text='1', padx=20, pady=20,
                 command=lambda: insertFunc(1))
button2 = Button(root, text='2', padx=20, pady=20,
                 command=lambda: insertFunc(2))
button3 = Button(root, text='3', padx=20, pady=20,
                 command=lambda: insertFunc(3))

# last row
ac = Button(root, text='AC', padx=20, pady=20, command=lambda: clear())
button0 = Button(root, text='0', padx=20, pady=20,
                 command=lambda: insertFunc(0))
buttonDot = Button(root, text='.', padx=20, pady=20,
                   command=lambda: insertFunc('.'))

# equal button
buttonEqual = Button(root, text='=', padx=20, pady=20,
                     command=lambda: equal(), state=DISABLED)


# show our widgets to the screen
entry.grid(column=0, row=0, sticky='wens',  columnspan=4)


# set our buttons
# first row
rest.grid(row=1, column=0, columnspan=1, sticky='wens', padx=5, pady=5)
multiply.grid(row=1, column=1, columnspan=1, sticky='wens', padx=5, pady=5)
divide.grid(row=1, column=2, columnspan=1, sticky='wens', padx=5, pady=5)
delete.grid(row=1, column=3, columnspan=1, sticky='wens', padx=5, pady=5)

# second row
button7.grid(row=2, column=0, columnspan=1, sticky='wens', padx=5, pady=5)
button8.grid(row=2, column=1, columnspan=1, sticky='wens', padx=5, pady=5)
button9.grid(row=2, column=2, columnspan=1, sticky='wens', padx=5, pady=5)
minus.grid(row=2, column=3, columnspan=1, sticky='wens', padx=5, pady=5)

# third row
button4.grid(row=3, column=0, columnspan=1, sticky='wens', padx=5, pady=5)
button5.grid(row=3, column=1, columnspan=1, sticky='wens', padx=5, pady=5)
button6.grid(row=3, column=2, columnspan=1, sticky='wens', padx=5, pady=5)
plus.grid(row=3, column=3, columnspan=1, sticky='wens', padx=5, pady=5)

# forth row
button1.grid(row=4, column=0, columnspan=1, sticky='wens', padx=5, pady=5)
button2.grid(row=4, column=1, columnspan=1, sticky='wens', padx=5, pady=5)
button3.grid(row=4, column=2, columnspan=1, sticky='wens', padx=5, pady=5)

# last row
ac.grid(row=5, column=0, columnspan=1, sticky='wens', padx=5, pady=5)
button0.grid(row=5, column=1, columnspan=1, sticky='wens', padx=5, pady=5)
buttonDot.grid(row=5, column=2, columnspan=1, sticky='wens', padx=5, pady=5)

# equal button
buttonEqual.grid(row=4, column=3, columnspan=1,
                 rowspan=2, sticky='wens', padx=5, pady=5)


# set our program title
root.title('WE Calculator')

# run our program
root.mainloop()
