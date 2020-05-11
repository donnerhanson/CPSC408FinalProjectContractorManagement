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
from updateTable import *
from Messages import *
from DisplayFunctions import *
from client import *
from csvHandler import *
from ImportToDatabase import *
from FakeData import *
from job import *
from parameterSearches import getInvoiceByJobID
from testingFuncs import *
from updateTable import *
from userInput import *
from parameterSearches import *

# main


start_time = time.time()

connection = mysql.connector.connect(host='35.247.37.38',
                                     database='ContractorManagementDB',
                                     user='Donner Hanson',
                                     password='DonnerPass1')


# TODO: "add in a logging system"
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
            userChoice = int(input(parameterLookupMenu))
            if userChoice == 1:
                userChoice = int(input(parameterJobLookup))
                if userChoice == 1:
                    salesChoice = input('Please enter the Job ID you wish to view:\n')
                    UsersOnJob(mycursor, salesChoice)
                elif userChoice == 2:
                    subChoice = input('Please enter the Job ID you wish to view:\n')
                    SubsOnJob(mycursor, subChoice)
                elif userChoice == 3:
                    invoiceChoice = input('Please enter the Job ID you wish to view:\n')
                    getInvoiceByJobID(mycursor, invoiceChoice)
                else:
                    print('Error, please enter a valid choice.')
                    continue
            elif userChoice == 2:
                userChoice = int(input(parameterClientLookup))
                if userChoice == 1:
                    jobChoice = input('Please enter the Client ID you wish to view:\n')
                    JobsOnClient(mycursor, jobChoice)
                elif userChoice == 2:
                    costChoice = input('Please enter the Client ID you wish to view:\n')
                    CostsOnClient(mycursor, costChoice)
                else:
                    print('Error, please enter a valid choice.')
                    continue
            elif userChoice == 3:
                userChoice = int(input(parameterContactLookup))
                if userChoice == 1:
                    jobChoice = input('Please enter the Contact ID you wish to view:\n')
                    JobsOnContact(mycursor, jobChoice)
                else:
                    print('Error, please enter a valid choice.')
                    continue
            elif userChoice == 4:
                userChoice = int(input(parameterUserLookup))
                if userChoice == 1:
                    jobChoice = input('Please enter the User ID you wish to view:\n')
                    JobsOnUsers(mycursor, jobChoice)
                else:
                    print('Error, please enter a valid choice.')
                    continue
            else:
                continue
            # could do things like:
            # find all jobs associated with personnel/clients
            # find all people associated with a job and job cost/total
            continue
        elif userChoice == 3:  # update Record TODO: Job/Job Cost in UpdateTable.py
            # client table update functioning as intended
            userChoice = int(input(update_table_prompt))
            userChoice = UpdateTable(connection, userChoice)
        elif userChoice == 4:  # create a record TODO: add users/employees
            userChoice = int(input('input\n 1 for add client:\n 2 for add user:\n'))
            if userChoice == 1:
                addClientAndJob(connection)
            elif userChoice == 2:
                addUser(mycursor)
        elif userChoice == 5:  # delete a record TODO: Implement SoftDeletes
            continue
        elif userChoice == 6:  # export structured CSV file
            exportDataBaseToCSV(mycursor)
            print('CSV exported')
            # could add separate parameterized CSVs to export using parameter functions
        else:
            print('Please enter a valid choice.\n')
            continue

connection.close()
print('Connection closed')

print(f"--- {time.time() - start_time} seconds ---")
