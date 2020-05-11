from Messages import *
import mysql.connector
from datetime import datetime

from inputParseFuncs import getNumberChoice


def addExistingClientJobToDB(connection):
    c = connection.cursor()
    clientID = input(clientIDprompt)
    Estimate = input(estimatePrompt)
    Payout = input(payoutPrompt)
    Hours = getNumberChoice(hoursPrompt)
    date = datetime.now()
    # "AddJob(IN ClientIDIn int, IN EstimateIn float, IN PayoutIn float, IN HoursIN float,IN DateIN datetime)"
    # print(Mats)
    # print(adds)
    args = (clientID, Estimate, Payout, Hours, date)
    # print('inserted %s', ''.join(str(args)))
    c.callproc('AddJob', args)
    return clientID

def addNewClientJobToDB(connection, clientID):
    c = connection.cursor()
    Estimate = input(estimatePrompt)
    Payout = input(payoutPrompt)
    Hours = getNumberChoice(hoursPrompt)
    date = datetime.now()
    # "AddJob(IN ClientIDIn int, IN EstimateIn float, IN PayoutIn float, IN HoursIN float,IN DateIN datetime)"
    # print(Mats)
    # print(adds)
    args = (clientID, Estimate, Payout, Hours, date)
    # print('inserted %s', ''.join(str(args)))
    c.callproc('AddJob', args)
    return clientID