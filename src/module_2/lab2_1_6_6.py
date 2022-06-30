fnam = input('Your first name: ')
lnam = input('Your last name: ')
print("Thanks.")
print()
# Normal print
print('Hello:', fnam, lnam)
# Another version
print('Hello', fnam, sep=": ", end=' ')
print(lnam)

# Lab 2.1.6.7
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end='')
print("+" + 10 * "-" + "+")
