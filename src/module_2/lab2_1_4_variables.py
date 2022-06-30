#
# variable naming conventions
#
# lower case and separated by underscores: snake_case
# Function names: same as the variable names
#
# Python is case-sensitive
var = "3.8.6"
print("Python version: ", var)

# Lab 2.1.4.6
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** .5
print("c = ", c)

# Lab 2.1.4.7
john = 3
mary = 5
adam = 6
print(john, mary, adam, sep=", ")
totalApples = john+mary+adam
print(totalApples)
print()
print('Total apples:', totalApples, sep=" ")

# Lab 2.1.4.8
i = 2
j = 3
i = i + 2 * j
print(i)

i = 2
i += 2 * j
print(i)

k = 10
k %= 4
print(k)  # 2

i = 3
i **= 3
print(i)  # 27
