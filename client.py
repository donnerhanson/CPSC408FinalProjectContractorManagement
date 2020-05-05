import mysql
import re

from Messages import *


def addClient(cursor):
    name = input(clientInName)
    address = input(addressInMessage)
    city = input(cityInMessage)
    state = input(stateInMessage)
    # doesnt check for !@#$%^&*() yet
    while len(state) > 2 or len(state) < 2 or re.search('[0-9]', state):
        state = input(stateInMessage)
    # zip length error check
    zipCode = input(zipInMessage)
    while len(zipCode) > 5 or len(zipCode) < 5 or re.search('[a-zA-Z]', zipCode):
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
    # return this to add a job for the new client
    return lastClientID


def CalculateNumJobsForClient(connection: mysql.connector, Client_ID: int):
    # updates single client when job added to existing client
    cursor = connection.cursor()
    query = """UPDATE Client SET NumJobs = (SELECT COUNT(*) from Job WHERE Job.Client_ID = %s)"""
    cursor.execute(query,(Client_ID,))
    connection.commit()
