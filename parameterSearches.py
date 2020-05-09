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
    if numChoice > str(lastJobID):
        print('Error, Job does not exist.')
    else:

        cursor.execute('SELECT DISTINCT J.JOB_ID, C.ClientName as Client_Name, '
                       'J.Client_ID, U.Name as Salesperson_Name, JSD.User_ID '
                       'FROM Job, Client, Users, JobSalesDetails JSD '
                       'INNER JOIN Job J on JSD.Job_ID = J.JOB_ID '
                       'INNER JOIN Users U on JSD.User_ID = U.User_ID '
                       'INNER JOIN Client C on J.Client_ID = C.Client_ID '
                       'WHERE J.JOB_ID = %s ORDER BY J.JOB_ID') % numChoice
        # """Select %s FROM table WHERE JOB_ID =  %s """ % (numChoice)
    return lastJobID
