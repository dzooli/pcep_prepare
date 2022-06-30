# Basic operators
print(2+2)
print(2*2+1)
print(1+2*2)
print(5//2)  # integer division
print(5 % 2)  # remainder division
print(5**2)  # power
print(2**2**3)

# operators result type
print(6 // 3)
print(6 // .3)
print(type(6 // .3))
print(6. // 4)
print(type(6. // 4))

# division by zero
try:
    print(2/0)
except ZeroDivisionError:
    print('Division by zero')

# Operator precedence
# Priority      Operator
# 1             +-
# 2             **
# 3             * / %
# 4             +, -
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print(2 ** 4, (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print(2 ** 3 ** 2)
