if __name__ == "__main__":
    from math import pi

    print(f"Original Pi is: {pi}\nRedefinition...")
    pi = 3.14
    print(f"Pi after redefinition: {pi}\nRe-import the original and assign the alias...")

    from math import pi as orig_pi

    print(f"Original Pi as orig_Pi is: {orig_pi}")
