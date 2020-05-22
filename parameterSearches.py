import mysql.connector
from mysql import connector

from Messages import *
from DisplayFunctions import *


def UsersOnJob(cursor, job_id):
    numChoice = job_id
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
    if int(numChoice) > lastJobID or int(numChoice) <= 0:
        print('Error, Job does not exist. Please enter a valid ID.')
    else:
        select_query = 'SELECT DISTINCT J.JOB_ID, C.ClientName as Client_Name, '\
                       'J.Client_ID, U.Name as Salesperson_Name, JSD.User_ID '\
                       'FROM Job, Client, Users, JobSalesDetails JSD '\
                       'INNER JOIN Job J on JSD.Job_ID = J.JOB_ID '\
                       'INNER JOIN Users U on JSD.User_ID = U.User_ID '\
                       'INNER JOIN Client C on J.Client_ID = C.Client_ID '\
                       'WHERE J.JOB_ID = %s ORDER BY J.JOB_ID' % numChoice
        cursor.execute(select_query, )
        printResultTable(cursor)
    return lastJobID

def SubsOnJob(cursor, job_id):
    numChoice = job_id
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
    if int(numChoice) > lastJobID or int(numChoice) <= 0:
        print('Error, Job does not exist. Please enter a valid ID.')
    else:
        select_query = 'SELECT DISTINCT J.JOB_ID, C.ClientName as Client_Name, '\
                       'J.Client_ID, CO.ContactName as Subcontractor_Name, JSD.Contact_ID '\
                       'FROM Job, Client, Contacts, JobSubDetails JSD '\
                       'INNER JOIN Job J on JSD.Job_ID = J.JOB_ID '\
                       'INNER JOIN Contacts CO on JSD.Contact_ID = CO.Contact_ID '\
                       'INNER JOIN Client C on J.Client_ID = C.Client_ID '\
                       'WHERE J.JOB_ID = %s ORDER BY J.JOB_ID' % numChoice
        cursor.execute(select_query, )
        printResultTable(cursor)
    return lastJobID

def JobsOnClient(cursor, client_id):
    numChoice = client_id
    cursor.execute("select Client_ID from Client ORDER BY Client_ID DESC LIMIT 1")  # get last user
    lastClientIDList = cursor.fetchall()  # returns a list with a tuple inside
    lastClientID = 0
    for value in lastClientIDList:  # iterate the list
        for num in value:  # iterate the tuple
            if num > 0:
                lastClientID = num
                break
            elif num is None:
                print('Client does not exist')
            else:
                print('something happened')
    if int(numChoice) > lastClientID or int(numChoice) <= 0:
        print('Error, Client does not exist. Please enter a valid ID.')
    else:
        select_query = 'SELECT DISTINCT C.Client_ID, C.ClientName, JOB_ID ' \
                       'FROM Client, Job ' \
                       'INNER JOIN Client C on Job.Client_ID = C.Client_ID ' \
                       'WHERE C.Client_ID = %s ' \
                       'ORDER BY C.Client_ID' %numChoice
        cursor.execute(select_query, )
        printResultTable(cursor)
    return lastClientID

def CostsOnClient(cursor, client_id):
    numChoice = client_id
    cursor.execute("select Client_ID from Client ORDER BY Client_ID DESC LIMIT 1")  # get last user
    lastClientIDList = cursor.fetchall()  # returns a list with a tuple inside
    lastClientID = 0
    for value in lastClientIDList:  # iterate the list
        for num in value:  # iterate the tuple
            if num > 0:
                lastClientID = num
                break
            elif num is None:
                print('Client does not exist')
            else:
                print('something happened')
    if int(numChoice) > lastClientID or int(numChoice) <= 0:
        print('Error, Client does not exist. Please enter a valid ID.')
    else:
        select_query = 'SELECT DISTINCT JC.Job_ID, J.Client_ID, Additions, MaterialsCost, ROUND(MaterialsCost+Additions, 2) AS Total_Invoice ' \
                       'FROM Job J ' \
                       'INNER JOIN JobCost JC ON J.JOB_ID = JC.Job_ID ' \
                       'INNER JOIN Job ON JC.Job_ID ' \
                       'WHERE J.Client_ID = %s;' %numChoice
        cursor.execute(select_query, )
        printResultTable(cursor)
    return lastClientID

def JobsOnContact(cursor, contact_id):
    numChoice = contact_id
    cursor.execute("select Contact_ID from Contacts ORDER BY Contact_ID DESC LIMIT 1")  # get last user
    lastContactIDList = cursor.fetchall()  # returns a list with a tuple inside
    lastContactID = 0
    for value in lastContactIDList:  # iterate the list
        for num in value:  # iterate the tuple
            if num > 0:
                lastContactID = num
                break
            elif num is None:
                print('Contact does not exist')
            else:
                print('something happened')
    if int(numChoice) > lastContactID or int(numChoice) <= 0:
        print('Error, Contact does not exist. Please enter a valid ID.')
    else:
        select_query = 'SELECT DISTINCT C.ContactName, C.Contact_ID, Job_ID ' \
                       'FROM Contacts, JobSubDetails ' \
                       'INNER JOIN Contacts C on JobSubDetails.Contact_ID = C.Contact_ID ' \
                       'WHERE C.Contact_ID = %s ' \
                       'ORDER BY C.Contact_ID' % numChoice
        cursor.execute(select_query, )
        printResultTable(cursor)
    return lastContactID

def JobsOnUsers(cursor, user_id):
    numChoice = user_id
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
    if int(numChoice) > lastUserID or int(numChoice) <= 0:
        print('Error, User does not exist. Please enter a valid ID.')
    else:
        select_query = 'SELECT DISTINCT U.Name, U.User_ID, Job_ID ' \
                       'FROM Users, JobSalesDetails ' \
                       'INNER JOIN Users U on JobSalesDetails.User_ID = U.User_ID ' \
                       'WHERE U.User_ID = %s ' \
                       'ORDER BY U.User_ID' % numChoice
        cursor.execute(select_query, )
        printResultTable(cursor)
    return lastUserID


# may need some sort of checking to make sure record exists
def getInvoiceByJobID(cursor, job_id):
    select_query = """SELECT DISTINCT JC.Job_ID, J.Client_ID, ROUND(MaterialsCost+Additions, 2) AS Total_Invoice,  Additions, MaterialsCost FROM Job J INNER JOIN JobCost JC ON J.JOB_ID = JC.Job_ID INNER JOIN Job ON JC.Job_ID WHERE J.JOB_ID = %s;""" % job_id
    cursor.execute(select_query, )
    printResultTable(cursor)

def getUsersByRole(cursor, role_id):
    numChoice = role_id
    select_query = 'SELECT * FROM UserView WHERE Role_ID = %s' %numChoice
    cursor.execute(select_query, )
    printResultTable(cursor)

def getContactsByCategory(cursor, cat_id):
    numChoice = cat_id
    select_query = 'SELECT * FROM ContactView WHERE CompanyCategory_ID = %s' %numChoice
    cursor.execute(select_query, )
    printResultTable(cursor)

