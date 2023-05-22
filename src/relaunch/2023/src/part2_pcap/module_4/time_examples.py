import time
from pprint import pprint

t1 = time.time()
ct1 = time.ctime(t1)
pprint(dir(ct1))
pprint(ct1)
print(f"Current time is: {time.ctime(t1)}")