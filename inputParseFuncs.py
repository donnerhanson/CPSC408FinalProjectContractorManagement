def getUserNumInt(string):
    while True:
        try:
            userIn = int(input(string))
        except ValueError:
            print ('Not a valid entry')
            continue
        else:
            return userIn


def getUserNumFloat(string):
    while True:
        try:
            userIn = float(input(string))
        except ValueError:
            print ('Not a valid entry')
            continue
        else:
            return userIn


def getStringIn(string):
    userIn = input(string)
    return userIn
