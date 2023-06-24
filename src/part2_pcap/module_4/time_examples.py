import time
from datetime import datetime
from pprint import pprint

t1 = time.time()
ct1 = time.ctime(t1)
pprint(dir(ct1))
pprint(ct1)
print(f"Current time is: {time.ctime(t1)}")

print('\ngmtime and localtime')
loct = time.localtime()
gmt = time.gmtime()
pprint(gmt)
pprint(loct)

print('\nasctime and mktime')
ts =time.time() + 7200
gm_timestruct = time.gmtime(ts)
at = time.asctime(gm_timestruct)
pprint(at)

created_time = time.mktime((2023, 11, 11, 10, 10, 10, 0, 0, 0))
pprint(type(created_time))
pprint(created_time)

print('\nCurrent date and time:')
pprint(datetime.today())
pprint(datetime.now())
pprint(datetime.utcnow())
pprint(datetime.timestamp(datetime.today()))

print("\ntime.strftime takes an additional time_struct parameter")
st = time.gmtime()
pprint(time.strftime("%Y/%m/%d", st))
