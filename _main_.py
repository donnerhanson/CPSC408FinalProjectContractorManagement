# Python 3.7
# Donner Hanson
# April 25 2020
# CPSC 408-01

# USERNAME Donner Hanson
# PASS DonnerPass1
import sys

import mysql.connector
import time

from csv import writer
import csv

# USER DEFINED FILES
from Messages import *
from DisplayFunctions import *
from client import *
from csvHandler import *
from ImportToDatabase import *
from FakeData import *
from job import *
from testingFuncs import *

# main


start_time = time.time()

connection = mysql.connector.connect(host='35.247.37.38',
                                     database='ContractorManagementDB',
                                     user='Donner Hanson',
                                     password='DonnerPass1')
clientIndex = 4


# ADD A NEW CLIENT AND JOB
def addClientAndJob(mysql_connection):
    cursor = mysql_connection.cursor()
    currClientID = addClient(cursor)
    addNewClientJobToDB(mysql_connection, currClientID)
    CalculateNumJobsForClient(mysql_connection, currClientID)


mycursor = connection.cursor()

mode = 0
while mode != 1 | mode != 2:
    mode = int(input('input mode:\n 1: fresh, 2: continual...\n '))

if int(mode) == 1:
    num_tuples = int(input('Enter the amount of clients and jobs: Ex: 9\n'))
    ResetDBToRandVals(connection, num_tuples)




# printAnyFullTable(mycursor, tableNamesAddOrder[4])
else:
    addClientAndJob(connection)

# printAnyFullTable(mycursor, tableNamesAddOrder[4])
# printJobCostCalculatedTable(mycursor)
exportDataBaseToCSV(mycursor)
print('CSV exported')

# printAnyFullTable(cursor, table_name):


# for i in tableNamesAddOrder:
#   printAnyFullTable(mycursor, i)


connection.close()
print('Connection closed')

print(f"--- {time.time() - start_time} seconds ---")
