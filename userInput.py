import mysql.connector
import re
from Messages import *

def addUser(cursor):
    name = input(userInName)
    role = input(userRoleIDIn)
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