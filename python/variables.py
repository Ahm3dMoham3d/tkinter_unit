# there is two ways to declare variables

# the first one
x = 5
y = "John"

# you can overwrite the variable value
x = 4       # x is of type int
x = "Sally"  # x is now of type str


# and the second way to declare a variable is by casting it
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# important
# Variable names are case-sensitive.
a = 4
A = "Sally"
# A will not overwrite a

# Legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Multi Words Variable Names

# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "John"


# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"

# Also, use the global keyword if you want to change a global variable inside a function.
x = "awesome"


def myfunc():
    global x  # now var x is accessible anywhere in the code
    x = "fantastic"


myfunc()
print("Python is " + x)


# Exercise
# https://www.w3schools.com/python/exercise.asp?filename=exercise_variables1
