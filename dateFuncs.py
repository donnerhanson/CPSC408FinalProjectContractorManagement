import calendar
from datetime import *

monthMessage = 'Enter the month (Ex: 11): \n'
dayMessage = 'Enter the day: \n'
yearMessage = 'Enter the year: \n'
monthError = 'Please enter a range between 01 and 12: \n'
yearError = 'Please enter a year in range (%s, %s):\n', (MINYEAR, MAXYEAR)

def getYear():
    year = int(input(yearMessage))
    while year <= MINYEAR or year >= MAXYEAR:
        print(yearError)
        year = int(input(monthMessage))
    return year


def getMonth():
    month = int(input(monthMessage))
    while month <= 0 or month > 12:
        print(monthError)
        month = int(input(monthMessage))
    return month


def getDay(year, month):
    last_day = int(calendar.monthrange(year, month)[1])
    dayError = 'Please enter in range 1-%s', last_day
    day = int(input(dayMessage))
    while day <= 0 or day > last_day:
        print(dayError)
        day = int(input(dayMessage))
    return day


def getDate():
    year = getYear()
    month = getMonth()
    day = getDay(year, month)
    hours = 0
    minutes = 0
    seconds = 0
    return datetime(year, month, day, hours, minutes, seconds)
