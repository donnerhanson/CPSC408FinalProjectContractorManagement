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
            return userIn
        except ValueError:
            print('Not a valid entry')
            return getUserNumFloat(string)


def getStringIn(string):
    userIn = input(string)
    return userIn


def is_only_nums(userChoice):  # returns false if NaN, True Otherwise
    if re.search('[a-zA-Z]', str(userChoice)):
        NumberInputError(userChoice)
        return False
    return True


def getWholeNumberChoice(message):
    userInput = -1
    while userInput == -1 or not is_only_nums(userInput):
        userInput = input(message)
    try:
        return int(userInput)
    except ValueError: # if floating point is put in
        print('Invalid entry: must be a whole number')
        return getWholeNumberChoice(message)
