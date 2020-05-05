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
from updateTable import *

# main


start_time = time.time()

connection = mysql.connector.connect(host='35.247.37.38',
                                     database='ContractorManagementDB',
                                     user='Donner Hanson',
                                     password='DonnerPass1')


# ADD A NEW CLIENT AND JOB
def addClientAndJob(mysql_connection):
    cursor = mysql_connection.cursor()
    currClientID = addClient(cursor)
    addNewClientJobToDB(mysql_connection, currClientID)
    CalculateNumJobsForClient(mysql_connection, currClientID)


mycursor = connection.cursor()

userChoice = 0
while userChoice != 1 and userChoice != 2:
    userChoice = int(input('input mode:\n 1: fresh, 2: continual...\n '))

if userChoice == 1:
    num_tuples = int(input('Enter the amount of clients and jobs: Ex: 9\n'))
    ResetDBToRandVals(connection, num_tuples)

# printAnyFullTable(mycursor, tableNamesAddOrder[4])
else:
    while userChoice != 0:
        userChoice = int(input(main_output_message))
        if userChoice == 1:  # display options - works for now - need to add if deleted dont show
            userChoice = int(input(DisplayTableMessage(table_names_drop_order)))
            printAnyFullTable(mycursor, table_names_drop_order[userChoice - 1])
        elif userChoice == 2:  # parameterized search
            continue
        elif userChoice == 3:  # update Record TODO: in progress working on clients in UpdateTable.py
            userChoice = int(input(update_table_prompt))
            UpdateTable(connection, userChoice)
            continue
        elif userChoice == 4:  # create a record TODO: add users/employees
            userChoice = int(input())
            addClientAndJob(connection)
        elif userChoice == 5:  # delete a record TODO: Implement SoftDeletes
            continue
        elif userChoice == 6:  # export CSV
            exportDataBaseToCSV(mycursor)
            print('CSV exported')
        else:
            continue

connection.close()
print('Connection closed')

print(f"--- {time.time() - start_time} seconds ---")
