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
                print('user does note exist')
            else:
                print('something happened')
    return lastUserID

def updateUser(cursor):
    updateNums = ''
    updateID = input('Please enter the ID of the User you wish to update: \n')
    updateNums = 'Please select the fields you wish to update: \n1. Name\n 2. Role ID\n 3. Address\n' \
                 '4. City\n 5. State\n 6. Zip\n 7. Phone\n 8. Email\n 0. Exit\n'
    while input(updateNums) != 0:
        if updateNums == 1:
            nameIn = input(userInName)
            cursor.execute('UPDATE Users SET Name = ' + nameIn + ' WHERE User_ID = ' + updateID)
            continue
        elif updateNums == 2:
            roleIn = input(userRoleIDIn)
            cursor.execute('UPDATE Users SET Role_ID = ' + roleIn + ' WHERE User_ID = ' + updateID)
            continue
        elif updateNums == 3:
            addressIn = input(addressInMessage)
            cursor.execute('UPDATE Users SET address = ' + addressIn + ' WHERE User_ID = ' + updateID)
            continue
        elif updateNums == 4:
            cityIn = input(cityInMessage)
            cursor.execute('UPDATE Users SET City = ' + cityIn + ' WHERE User_ID = ' + updateID)
            continue
        elif updateNums == 5:
            stateIn = input(stateInMessage)
            if len(stateIn) != 2:
                print('Error, please enter the State in the following format: \'CA\'')
            else:
                cursor.execute('UPDATE Users SET State = ' + stateIn + ' WHERE User_ID = ' + updateID)
            continue
        elif updateNums == 6:
            zipIn = input(zipInMessage)
            if len(zipIn) != 5:
                print('Error, Zip code must be 5 characters long.')
            else:
                cursor.execute('UPDATE Users SET Zip = ' + zipIn + ' WHERE User_ID = ' + updateID)
            continue
        elif updateNums == 7:
            phoneIn = input(phoneInMessage)
            cursor.execute('UPDATE Users SET Phone = ' + phoneIn + ' WHERE User_ID = ' + updateID)
            continue
        elif updateNums == 8:
            emailIn = input(emailInMessage)
            cursor.execute('UPDATE Users SET Email = ' + emailIn + ' WHERE User_ID = ' + updateID)
            continue
        else:
            return
        return

