import math

print(dir(math))

import random as rnd 

try:
    print(dir(random))
except NameError:
    print("\nrandom is not defined but aliased")
    print(dir(rnd))

