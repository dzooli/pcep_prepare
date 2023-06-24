import math


def sin(x):
    print("\nThis is my sin() function in the program's namespace.")
    return (math.sin(x * (math.pi / 180.0)))


if __name__ == "__main__":
    print("Sin() from the math module...\nmath.sin(2): ", math.sin(2 * (math.pi / 180.0)))
    print("own sin(2)", sin(2))
