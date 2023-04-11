
print("first assert")
a = 2
assert a, "a is zero"

print("second assert")
a = 0
try:
    assert a, "a is zero"
except AssertionError:
    print("Assert failed - but exception handled")

print("assert by None")
x = None
assert x, "assertion failed: x is None"
