import calendar
from datetime import *

from inputParseFuncs import getNumberChoice

monthMessage = 'Enter the month (Ex: 11): \n'
dayMessage = 'Enter the day: \n'
yearMessage = 'Enter the year: \n'
monthError = 'Please enter a range between 01 and 12: \n'
yearError = 'Please enter a year in range (%s, %s):\n', (MINYEAR, MAXYEAR)


def getYear():
    year = getNumberChoice(yearMessage)
    while year <= MINYEAR or year >= MAXYEAR:
        print(yearError)
        year = getNumberChoice(monthMessage)
    return year


def getMonth():
    month = getNumberChoice(monthMessage)
    while month <= 0 or month > 12:
        print(monthError)
        month = getNumberChoice(monthMessage)
    return month


def getDay(year, month):
    last_day = int(calendar.monthrange(year, month)[1])
    dayError = 'Please enter in range 1-%s', last_day
    day = getNumberChoice(dayMessage)
    while day <= 0 or day > last_day:
        print(dayError)
        day = getNumberChoice(dayMessage)
    return day


def getDate():
    year = getYear()
    month = getMonth()
    day = getDay(year, month)
    hours = 0
    minutes = 0
    seconds = 0
    return datetime(year, month, day, hours, minutes, seconds)
