import re

from Messages import NumberInputError


def getUserNumInt(string):
    while True:
        try:
            userIn = int(input(string))
        except ValueError:
            print('Not a valid entry')
            continue
        else:
            return userIn


def getUserNumFloat(string):
    while True:
        try:
            userIn = float(input(string))
        except ValueError:
            print('Not a valid entry')
            continue
        else:
            return userIn


def getStringIn(string):
    userIn = input(string)
    return userIn


def is_only_nums(userChoice):  # returns false if NaN, True Otherwise
    if re.search('[a-zA-Z]', str(userChoice)):
        NumberInputError(userChoice)
        return False
    return True


def getNumberChoice(message):
    userInput = -1
    while userInput == -1 or not is_only_nums(userInput):
        userInput = input(message)
    return int(userInput)
