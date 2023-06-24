import calendar
from calendar import Calendar


class CountingCalendar(Calendar):
    def __init__(self, first: int):
        super().__init__(first)

    def count_weekday_in_year(self, year: int, weekday: int):
        result = set()
        for month in range(1, 13):
            for day in self.itermonthdays4(year, month):
                if day[3] == weekday and day[0] == year:
                    result.add(day)
        return len(result)


mycal = CountingCalendar(calendar.MONDAY)
print(mycal.count_weekday_in_year(2019, 0))
print(mycal.count_weekday_in_year(2000, 6))

calendar.prmonth(2023, 6)
