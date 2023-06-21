"""
  lambda examples
"""

sqr = lambda x: x * x
print(sqr(2))


def print_function(*args, fun):
    func_args = args[0]
    print(f"function: {fun.__name__}{func_args}) returns {fun(func_args)}")


def myfun(i: int):
    print(f"Called with: {i}")
    return 2 * int(i)


print("Function information using standard function definition:")
print_function(12, fun=myfun)
print()

print("Function definition using lambda:")
for i in range(4):
    print_function(i, fun=(lambda x: int(x) * 2))

f1 = lambda x, y: (x * 2, y * 3)
print(f1(3, 4))

foo = filter(lambda x: x == 1, [1, 2, 3])
print(list(foo))


def I():
    s = "abcdef"
    for c in s[::2]:
        yield c


for x in I():
    print(x, end="")


print()
def fun(n):
    s = "+"
    for i in range(n):
        s += s
        print(f"i: {i}, s: {s}")
        yield s

for x in fun(2):
    # print(x, end="")
    pass
