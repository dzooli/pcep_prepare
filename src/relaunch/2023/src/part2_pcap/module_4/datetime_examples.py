import datetime
import time
from datetime import date
from pprint import pprint

pprint(date.today())
pprint(timenow := time.time())
pprint(datenow := datetime.date.fromtimestamp(timenow))
pprint(datenow.timetuple())

print(f"fromiso:")
d1 = date.fromisoformat("2023-05-12")
pprint(d1.ctime())
pprint(d1.timetuple())
pprint(d1.strftime("%Y-%m-%d-%H:%M:%S"))

print()
weekdays = ['Hétfő', "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", 'Vasárnap']
print(f"Ma {weekdays[date.today().weekday()]} van.")
print(f"Ma a hét {date.today().isoweekday()}. napja van.")