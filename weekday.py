# weekday counter implementation
from enum import Enum


class WrongInputException(Exception):
    pass


class Weekday(Enum):
    Mon = 0
    Tue = 1
    Wed = 2
    Thu = 3
    Fri = 4
    Sat = 5
    Sun = 6


def count_weekday(year, month, day):
    pass

