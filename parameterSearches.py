import mysql.connector
from Messages import *


def UsersOnJob(cursor):
    numChoice = input('Please enter the Job ID you wish to view:\n')
    cursor.execute("select JOB_ID from Job ORDER BY JOB_ID DESC LIMIT 1")  # get last user
    lastJobIDList = cursor.fetchall()  # returns a list with a tuple inside
    lastJobID = 0
    for value in lastJobIDList:  # iterate the list
        for num in value:  # iterate the tuple
            if num > 0:
                lastJobID = num
                break
            elif num is None:
                print('Job does not exist')
            else:
                print('something happened')
    if numChoice > lastJobID:
        print('Error, Job does not exist.')
    else:
        cursor.execute('select')
    return lastJobID
