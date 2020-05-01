# Python 3.7
# Donner Hanson
# April 25 2020
# CPSC 408-01

# USERNAME Donner Hanson
# PASS DonnerPass1
import sys

import mysql.connector

from csv import writer
import csv

from pandas import DataFrame

# USER DEFINED FILES
from Messages import *
from DisplayFunctions import *
from client import *
from csvHandler import *
from ImportToDatabase import *
from FakeData import *
from job import *
import mysql.connector
import time

# main


start_time = time.time()

connection = mysql.connector.connect(host='35.247.37.38',
                                     database='ContractorManagementDB',
                                     user='Donner Hanson',
                                     password='DonnerPass1')
clientIndex = 4

num_entries = 9


# ADD A NEW CLIENT AND JOB
def addClientAndJob(mysql_connection):
    cursor = mysql_connection.cursor()
    currClientID = addClient(cursor)
    addNewClientJobToDB(mysql_connection, currClientID)
    CalculateNumJobsForClient(mysql_connection, currClientID)


mycursor = connection.cursor()
print('Resetting Database')
mycursor.callproc('FRESHDATABASE')
print('DataBase reset')

tableNamesAddOrder = ('Roles', 'CompanyCategoryTableLookup', 'StatusDefinition',
                      'Users', 'Client', 'Contacts', 'Job', 'JobCost',
                      'JobSubDetails', 'JobStatus', 'JobSalesDetails')

# FAKE DATA GENERATOR NOT TO OR FROM CSV - Used in main project testing
# printAnyTable(mycursor, tableNamesAddOrder[2])
print('Running Fake Data Generation')
addFakeRolesToDB(mycursor)
print('Roles added')

addFakeClientsToDB(mycursor, num_entries)
# printClientTable(mycursor)  # Includes Field Header names
print('Clients added')
addFakeCompanyCategoryIDToDB(mycursor)  # done
# printCompanyCategoryTableLookup(mycursor)
print('Company Category table lookup added')
addFakeStatusDefinitionToDB(mycursor, num_entries)  # done
# printAnyTable(mycursor, tableNamesAddOrder[2])
print('status def added')
addFakeJobToDB(mycursor)  # Links to all available clients
print('jobs added')
addFakeJobCostToDB(mycursor)  # links to all available jobs
print('job cost added')
addFakeContacts(mycursor, num_entries)
print('contacts should be added')
addFakeUsers(mycursor, num_entries)
print('users Should be added')
CalculateNumJobsForRandClients(connection)
print('rand num')
# printAnyFullTable(mycursor, tableNamesAddOrder[4])

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
