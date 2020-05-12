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
from SoftDelete import SoftDelete
from inputParseFuncs import is_only_nums, getWholeNumberChoice
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


# TODO: INDEXING, DATABASE VIEWS, FORMATTING CHECK,
#
#  TODO: (OPTIONAL FEATURES): Login Input Information, LOGGING SYSTEM

start_time = time.time()

connection = mysql.connector.connect(host='35.247.37.38',
                                     database='ContractorManagementDB',
                                     user='Donner Hanson',
                                     password='DonnerPass1')


# TODO: "add in a logging system" if we have time



mycursor = connection.cursor()
userChoice = -1
while userChoice != 1 and userChoice != 2:
    userChoice = getWholeNumberChoice('input mode:\n 1: fresh, 2: continual...\n ')

if userChoice == 1:  # fresh DB must have at least one record
    num_tuples = -1
    while num_tuples <= 1:
        num_tuples = getWholeNumberChoice('Enter the amount of clients and jobs: Ex: 9\n')
    ResetDBToRandVals(connection, num_tuples)

# printAnyFullTable(mycursor, tableNamesAddOrder[4])
else:
    while userChoice != 0:
        userChoice = getWholeNumberChoice(main_output_message)
        if userChoice == 1:  # display options - works for now - need to add if deleted dont show
            userChoice = getWholeNumberChoice((DisplayTableMessage(table_names_drop_order)))
            if not userChoice > len(table_names_drop_order):
                printAnyFullTable(mycursor, table_names_drop_order[userChoice - 1])
            elif userChoice == 12:
                avgJobCost(mycursor)
            else:
                print("invalid entry")
        elif userChoice == 2:  # parameterized search
            userChoice = getWholeNumberChoice(parameterLookupMenu)
            if userChoice == 1:
                userChoice = getWholeNumberChoice(parameterJobLookup)
                if userChoice == 1:
                    salesChoice = getWholeNumberChoice('Please enter the Job ID you wish to view:\n')
                    UsersOnJob(mycursor, salesChoice)
                elif userChoice == 2:
                    subChoice = getWholeNumberChoice('Please enter the Job ID you wish to view:\n')
                    SubsOnJob(mycursor, subChoice)
                elif userChoice == 3:
                    invoiceChoice = getWholeNumberChoice('Please enter the Job ID you wish to view:\n')
                    getInvoiceByJobID(mycursor, invoiceChoice)
                elif userChoice == 4:
                    avgJobCostGreater(mycursor)
                elif userChoice == 5:
                    avgJobCostLesser(mycursor)
                else:
                    print('Error, please enter a valid choice.')
                    continue
            elif userChoice == 2:
                userChoice = getWholeNumberChoice(parameterClientLookup)
                if userChoice == 1:
                    jobChoice = getWholeNumberChoice('Please enter the Client ID you wish to view:\n')
                    JobsOnClient(mycursor, jobChoice)
                elif userChoice == 2:
                    costChoice = getWholeNumberChoice('Please enter the Client ID you wish to view:\n')
                    CostsOnClient(mycursor, costChoice)
                else:
                    print('Error, please enter a valid choice.')
                    continue
            elif userChoice == 3:
                userChoice = getWholeNumberChoice(parameterContactLookup)
                if userChoice == 1:
                    jobChoice = getWholeNumberChoice('Please enter the Contact ID you wish to view:\n')
                    JobsOnContact(mycursor, jobChoice)
                else:
                    print('Error, please enter a valid choice.')
                    continue
            elif userChoice == 4:
                userChoice = getWholeNumberChoice(parameterUserLookup)
                if userChoice == 1:
                    jobChoice = getWholeNumberChoice('Please enter the User ID you wish to view:\n')
                    JobsOnUsers(mycursor, jobChoice)
                else:
                    print('Error, please enter a valid choice.')
                    continue
            else:  # TODO: Ori check out why your function exits the program put this here as a quick fix
                userChoice = -1
                continue
            # could do things like:
            # find all jobs associated with personnel/clients
            # find all people associated with a job and job cost/total
        elif userChoice == 3:  # update Record TODO: Job/Job Cost in UpdateTable.py
            # client table update functioning as intended
            userChoice = getWholeNumberChoice(update_table_prompt)
            userChoice = UpdateTable(connection, userChoice)
        elif userChoice == 4:  # create a record TODO: add users/employees
            userChoice = getWholeNumberChoice(add_person_prompt)
            if userChoice == 1:
                addClientAndJob(connection)
            elif userChoice == 2:
                addUser(mycursor)
            elif userChoice == 3:
                addExistingClientJobToDB(connection)
        elif userChoice == 5:  # delete a record TODO: Implement SoftDeletes
            SoftDelete(connection)
        elif userChoice == 6:  # export structured CSV file
            exportDataBaseToCSV(mycursor)
            print('CSV exported')
            # could add separate parameterized CSVs to export using parameter functions
        elif 0 < userChoice >= 7:
            print('Please enter a valid choice.\n')
        else:
            continue

connection.close()
print('Connection closed')

print(f"--- {time.time() - start_time} seconds ---")
