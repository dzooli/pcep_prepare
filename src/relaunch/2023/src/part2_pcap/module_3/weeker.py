class Weeker:
    __days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day_name: str = 'Mon'):
        if day_name not in self.__days:
            raise ValueError('Invalid day name')
        self._day_number = self.__days.index(day_name)

    def add_days(self, days: int = 0):
        self._day_number += days
        self._day_number %= 7

    def substract_days(self, days: int = 0):
        self.add_days(-days)

    def __str__(self):
        return self.__days[self._day_number]


if __name__ == "__main__":
    try:
        weeker = Weeker('Gux')
    except:
        pass
    weeker = Weeker()
    weeker.add_days(2)
    weeker.substract_days(4)
    print(weeker)
    weeker = Weeker('Sat')
    weeker.add_days(2)  # Mon
    weeker.substract_days(5)  # Wed
    print(weeker)
