import calendar
import datetime

days = [
    "Hétfő",
    "Kedd",
    "Szerda",
    "Csütörtök",
    "Péntek",
    "Szombat",
    "Vasárnap",
    "Nincs",
]

mycal = calendar.TextCalendar(calendar.MONDAY)
curdate = datetime.date.today()
mycal.prmonth(curdate.year, curdate.month, w=4)

for day in mycal.itermonthdays(2023, 6):
    print(day, end=" ")

for day in mycal.itermonthdays2(2023, 6):
    print(
        day[0], days[calendar.weekday(2023, 6, day[0]) if day[0] != 0 else 7], sep=": "
    )

print("\n")
for day in mycal.itermonthdays3(2023, 6):
    print(day)

print('\n')
for day in mycal.itermonthdays4(2023, 6):
    print(day, days[day[3]])
