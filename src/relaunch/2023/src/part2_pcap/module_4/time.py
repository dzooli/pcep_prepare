import time
from datetime import datetime, timedelta
from pprint import pprint

timestamp = int(time.time())

st = time.gmtime(timestamp)
print("Time struct:", st)

print("Timestamp to ISO (asctime):", time.asctime(st))  # timetamp to ISO string
print("Tuple to stamp (mktime):", time.mktime((2019, 11, 12, 14, 53, 0, 0, 308, 0)))  # time tuple to timestamp

mydate = datetime(2023, 6, 3, 16, 47, 0, 0, None)
pprint(mydate)
pprint(mydate.date())
pprint(mydate.time())
pprint(mydate.date().isoformat())
pprint(mydate.time().isoformat())
pprint(mydate.timestamp())

print("strftime examples")
pprint(mydate.strftime('%B/%d/%Y'))
pprint(time.strftime('%H:%M'))
print("strftime from time module accepts a time tuple:")
pprint(time.strftime('%H:%M', st))

print("\nParsing timestamp: 2023/04/11 21:00:00")
parsed = datetime.strptime("2023/04/11 21:00:00", '%Y/%m/%d %H:%M:%S')
print(parsed)
print(type(parsed))

print("\ndate operations:")
cdate = datetime.now()
year3 = datetime.now().replace((2020))
diff = cdate - year3
pprint(diff)
print(type(diff))

print("\ncrating timedelta...")
delta = timedelta(weeks=4)
print("Date 4 weeks before:", cdate - delta)
pprint(delta)
pprint(dir(delta), indent=4, compact=True)

