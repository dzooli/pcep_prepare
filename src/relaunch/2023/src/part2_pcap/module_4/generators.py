"""
  Generator examples
"""

def pow2(max_power):
    power = 1
    for n in range(max_power):
        power *= 2
        yield power


if __name__ == '__main__':
    for val in pow2(8):
        print(val)