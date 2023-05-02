"""
  lambda examples
"""


sqr = lambda x: x*x
print(sqr(2))


def print_function(*args, fun):
    func_args = args[0]
    print(f"function: {fun.__name__}{func_args}) returns {fun(func_args)}")


def myfun(i: int):
    print(f"Called with: {i}")
    return 2*int(i)


print("Function information using standard function definition:")
print_function(12, fun=myfun)
print()

print("Function definition using lambda:")
for i in range(4):
    print_function(i, fun=(lambda x: int(x)*2))
