from datetime import datetime


class Date:
    def __init__(self, date: datetime = None, date_dict: dict = None):
        self.__date_time = date if date is not None else datetime(
            year=date_dict['year'],
            month=date_dict['month'],
            day=date_dict['day'],
            hour=date_dict['hour'],
            minute=date_dict['minute'],
            second=date_dict['second']
        )

    @property
    def year(self):
        return self.__date_time.year

    @property
    def month(self):
        return self.__date_time.month

    @property
    def day(self):
        return self.__date_time.day

    @property
    def hour(self):
        return self.__date_time.hour

    @property
    def minute(self):
        return self.__date_time.minute

    @property
    def second(self):
        return self.__date_time.second

    def broken(self) -> dict:
        return {
            'year': self.year,
            'month': self.month,
            'day': self.day,
            'hour': self.hour,
            'minute': self.minute,
            'second': self.second
        }

    def cet_to_brl(self):
        self.__date_time += 3

    def brl_to_cet(self):
        self.__date_time -= 3

    def __add__(self, other: "Date"):
        self.__date_time += other.__date_time

    def __sub__(self, other):
        self.__date_time -= other.__date_time

