from math import exp

try:
    a = 1 / 0
except ZeroDivisionError:
    print("zero division")

try:
    a = 1 / 0
    print("not executed statement")
except ArithmeticError:
    print("arithmetic zero division - caught first as the parent of ZeroDivisionError")
except ZeroDivisionError:
    print("concrete zero division")

try:
    a = 1 / 0
except ZeroDivisionError:  # the more concrete first
    print("zero division - concrete")
except ArithmeticError:
    print("arithmetic error - more general")


# The code prints subsequent
# values of exp(k), k = 1, 2, 4, 8, 16, ...

ex = 1

try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('The number is too big.')

my_var = 1
assert my_var == 0
