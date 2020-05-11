import mysql.connector
import re
from Messages import *
from DisplayFunctions import printAnyFullTable
from inputParseFuncs import getNumberChoice


def addUser(cursor): #TODO: ORI - you need to check your inputs and validate user input data. I set num_roles up to make sure that \
    #                   roles are accurate in case more roles are added. The method below shows the workflow
    name = input(userInName)
    num_roles = getRoles(cursor)
    role = 0
    while (role <= 0) or (role > num_roles):
        role = getNumberChoice(userRoleIDIn)
    address = input(addressInMessage)
    city = input(cityInMessage)
    state = input(stateInMessage)
    # doesn't check for non-numeric/alphabetical characters yet
    while len(state) > 2 or len(state) < 2 or re.search('[0-9]', state):
        state = input(stateInMessage)
    # zip length error check
    zipCode = input(zipInMessage)
    while len(zipCode) > 5 or len(zipCode) < 5 or re.search('[a-zA-Z]', zipCode):
        zipCode = input(zipInMessage)
    phone = input(phoneInMessage)
    email = input(emailInMessage)
    args = [name, role, address, city, state, zipCode,
            phone, email]
    cursor.callproc('CreateUser', args)
    print('User created, returning to Menu...')
    cursor.execute("select User_ID from Users ORDER BY User_ID DESC LIMIT 1")  # get last user
    lastUserIDList = cursor.fetchall()  # returns a list with a tuple inside
    lastUserID = 0
    for value in lastUserIDList:  # iterate the list
        for num in value:  # iterate the tuple
            if num > 0:
                lastUserID = num
                break
            elif num is None:
                print('User does not exist')
            else:
                print('something happened')
    return lastUserID


def getRoles(cursor):
    return printAnyFullTable(cursor, 'Roles');
