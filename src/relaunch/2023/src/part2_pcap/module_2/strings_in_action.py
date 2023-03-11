str1 = "0122"
str2 = 122

try:
    print("equal" if str1 <= str2 else "not equal")
except TypeError:
    print("Comparing is not possible!")

mylist = ['kappa', 'gamma', 'alpha']
print("list.sort()")
print(mylist.sort())
print("sorted(list)")
print(sorted(mylist))

print("Conversion...")
print(int("123"))
print("Bad conversion")
try:
    print(int("123a"))
except ValueError as ex:
    print(str(ex))

print("String by number: 'aleph' < '1000'")
print('aleph' < '1000')
print("String by number: 'Aleph' < '1000'")
print('Aleph'<'1000')
