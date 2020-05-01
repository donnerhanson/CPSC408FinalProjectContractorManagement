import mysql

from Messages import *


def addClient(cursor):
    # fake.name(), fake.street_address(), fake.city(), fake.state_abbr(), fake.postcode(), fake.email(), fake.phone_number()

    name = input(clientInName)
    address = input(addressInMessage)
    city = input(cityInMessage)
    state = input(stateInMessage)
    zipCode = input(zipInMessage)
    email = input(emailInMessage)
    phone = input(phoneInMessage)
    args = [name, address, city, state, zipCode,
            email, phone]
    cursor.callproc('AddClient', args)
    cursor.execute("select Client_ID from Client ORDER BY Client_ID DESC LIMIT 1")  # get last Client
    lastClientIDList = cursor.fetchall()  # returns a list with a tuple inside
    lastClientID = 0
    for value in lastClientIDList:  # iterate the list
        for num in value:  # iterate the tuple
            if num > 0:
                lastClientID = num
                break
            elif num is None:
                print('no jobs available')
            else:
                print('something happened')
    return lastClientID


def CalculateNumJobsForClient(connection: mysql.connector, Client_ID: int):
    # updates all rows
    cursor = connection.cursor()
    print(Client_ID)
    query = """UPDATE Client SET NumJobs = (SELECT COUNT(*) from Job WHERE Job.Client_ID = %s)"""
    cursor.execute(query,(Client_ID,))
    connection.commit()
