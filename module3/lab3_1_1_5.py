# 3.1.1.5
n = int(input('Input for n greater or equal to 100: '))
print(n >= 100)

# 3.1.1.9
n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))
if n1 > n2 and n1 > n3:
    largest = n1
elif n2 > n1 and n2 > n3:
    largest = n2
elif n3 > n1 and n3 > n2:
    largest = n3
print('The largest number is:', largest)

# 3.1.1.10
print('Largest with max():', max(n1, n2, n3))

# 3.1.1.11
# TBC(ontinued)
