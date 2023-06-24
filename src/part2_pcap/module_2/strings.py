"""String related examples
"""

# strings are immutable
string1 = "Hello World!"
try:
    string1[0] = 'h'
except TypeError as ex:
    print(ex)
finally:        
    print(string1)


# ord()
print(f"Ordinal of 'H': {ord('H')}")
# chr()
print(f"Character with code 64 is: {chr(64)}")


# string slicing
print(string1[:5])
print(string1[3:5])
print(string1[-1:0:-1])
string2 = string1[0] + string1
print(string2[-1:0:-1])


# in operator
print(f"Hello in string1: {'Hello' in string1}")
print(f"hello in string1: {'hello' in string1}")
print(f"llo in string1: {'llo' in string1}")


# del operator
# strings are immutable !!!
try:
    del string1[0]
except TypeError as ex:
    print(ex)
finally:
    print(string1)

try:
    string1.append('B')
except AttributeError as ex:
    print(ex)

try:
    string1.insert(0, 'H')
except AttributeError as ex:
    print(ex)

# Demonstrating min() - Example 1:
print(min("AabByYzZ"))


# Search for...
string1 = 'Halmafa'
print(string1.index('a')) # Should be 1
try:
    print(string1.index('x')) # Exception, not found
except ValueError as ex:
    print(ex)


# Counting
string1 = 'aabbc'
print(string1)
print(f"count of 'a's: {string1.count('a')}")
print(f"count of 'x's: {string1.count('x')}") # No error, returns 0


print(string1.isupper())

