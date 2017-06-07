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


def get_month_code(month):
    if month == 1:
        return 0
    if month == 2 or month == 3 or month == 11:
        return 3
    if month == 4 or month == 7:
        return 6
    if month == 5:
        return 1
    if month == 6:
        return 4
    if month == 8:
        return 2
    if month == 9 or month == 12:
        return 5


def get_century_code(year):
    if 1700 < year < 1800 or 2100 <= year < 2200:
        return 4
    if 1800 <= year < 1900 or 2200 <= year < 2300:
        return 2
    if 1900 <= year < 2000 or year > 2300:
        return 0
    if 2000 <= year < 2100:
        return 6


def check_input(year, month, day):
    if type(year) is not int or type(month) is not int or type(day) is not int:
        raise WrongInputException
    if year < 0 or 12 < month or month < 0 or 31 < day or day < 0:
        return -1


def count_weekday(year, month, day):
    try:
        if check_input(year, month, day) == -1:
            return None
    except WrongInputException:
        raise WrongInputException
    years_last_digits = year % 100
    year_code = (years_last_digits + years_last_digits / 4) % 7
    month_code = get_month_code(month)
    if year % 4 == 0:
        leap = -1
    else:
        leap = 0
    century_code = get_century_code(year)
    return int(((year_code + month_code + century_code + day + leap) % 7) - 1)


