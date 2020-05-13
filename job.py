from Messages import *
import mysql.connector
from DisplayFunctions import printAnyFullTable
from datetime import datetime

from client import addClient, CalculateNumJobsForClient
from updateTable import RecordExistsOneCondition, RecordExistsTwoCondition
from inputParseFuncs import getWholeNumberChoice


def addExistingClientJobToDB(connection):
    c = connection.cursor()
    clientID = getWholeNumberChoice(clientIDprompt)
    while not RecordExistsOneCondition(connection, 'Client', 'Client_ID', clientID):
        print(dne_error_enter)
        clientID = getWholeNumberChoice(clientIDprompt)
    Estimate = input(estimatePrompt)
    Payout = input(payoutPrompt)
    Hours = getWholeNumberChoice(hoursPrompt)
    date = datetime.now()
    # "AddJob(IN ClientIDIn int, IN EstimateIn float, IN PayoutIn float, IN HoursIN float,IN DateIN datetime)"
    # print(Mats)
    # print(adds)
    args = (clientID, Estimate, Payout, Hours, date)
    # TODO: LINK Subcontractors and SalesPeople

    sub_id = getWholeNumberChoice('Enter Sub-Contractor Contact ID:\n')
    while not RecordExistsOneCondition(connection, 'Contacts', 'Contact_ID', sub_id):
        print("Invalid ID")
        sub_id = getWholeNumberChoice('Enter Sub-Contractor Contact ID:\n')

    sales_id = getWholeNumberChoice('Enter Sales ID:\n')
    while not RecordExistsTwoCondition(connection, 'Users', 'User_ID', sales_id, 'Role_ID', 1):
        print("Invalid ID")
        sales_id = getWholeNumberChoice('Enter Sales ID:\n')

    c.callproc('AddJob', args)

    query = """Select Job_ID from Job Order By Job_ID DESC LIMIT  1"""
    last_job_id = ExtractSingleSelectValue(c, query)

    args_sub = (last_job_id, sub_id)

    args_sales = (last_job_id, sales_id)

    c.callproc('CreateJobSubDetails', args_sub)

    c.callproc('CreateJobSalesDetails', args_sales)
    CalculateNumJobsForClient(connection, clientID)
    return clientID


# ADD A NEW CLIENT AND JOB
def addClientAndJob(mysql_connection):
    cursor = mysql_connection.cursor()
    currClientID = addClient(cursor)
    addNewClientJobToDB(mysql_connection, currClientID)
    CalculateNumJobsForClient(mysql_connection, currClientID)


def addNewClientJobToDB(connection, clientID):
    c = connection.cursor()
    Estimate = input(estimatePrompt)
    Payout = input(payoutPrompt)
    Hours = getWholeNumberChoice(hoursPrompt)
    date = datetime.now()
    # "AddJob(IN ClientIDIn int, IN EstimateIn float, IN PayoutIn float, IN HoursIN float,IN DateIN datetime)"
    # print(Mats)
    # print(adds)
    args = (clientID, Estimate, Payout, Hours, date)
    # print('inserted %s', ''.join(str(args)))
    c.callproc('AddJob', args)
    return clientID


def ExtractSingleSelectValue(cursor, query):
    cursor.execute(query)
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
