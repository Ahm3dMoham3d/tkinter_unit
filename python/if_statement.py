# how to declare an if statement
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# we can also declare it with one line statement
if a > b:
    print("a is greater than b")

# and we have the short hand if
print("A") if a > b else print("B")

# we have also [AND , OR , NOT] our logical operators
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

if a > b or c > a:
    print("At least one of the conditions is True")

if not a > b:
    print("a is NOT greater than b")

# Exercise
# https://www.w3schools.com/python/exercise.asp?filename=exercise_ifelse1#
