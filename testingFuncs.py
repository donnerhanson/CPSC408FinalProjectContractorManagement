from FakeData import *
from mysql import *


def ResetDBToRandVals(connector, num_entries):
    cursor = connector.cursor()
    print('Resetting Database')
    cursor.callproc('FRESHDATABASE')
    print('DataBase reset')

    tableNamesAddOrder = ('Roles', 'CompanyCategoryTableLookup', 'StatusDefinition',
                          'Users', 'Client', 'Contacts', 'Job', 'JobCost',
                          'JobSubDetails', 'JobStatus', 'JobSalesDetails')

    # FAKE DATA GENERATOR NOT TO OR FROM CSV - Used in main project testing
    # printAnyTable(cursor, tableNamesAddOrder[2])
    print('Running Fake Data Generation')
    addFakeRolesToDB(cursor)
    print('Roles added')

    addFakeClientsToDB(cursor, num_entries)
    # printClientTable(cursor)  # Includes Field Header names
    print('Clients added')
    addFakeCompanyCategoryIDToDB(cursor)  # done
    # printCompanyCategoryTableLookup(cursor)
    print('Company Category table lookup added')
    addFakeStatusDefinitionToDB(cursor, num_entries)  # done
    # printAnyTable(cursor, tableNamesAddOrder[2])
    print('status def added')
    addFakeJobToDB(cursor)  # Links to all available clients
    print('jobs added')
    addFakeJobCostToDB(cursor)  # links to all available jobs
    print('job cost added')
    addFakeContacts(cursor, num_entries)
    print('contacts added')
    addFakeJobSubDetails(cursor)
    print('fake job sub under construction')
    addFakeUsers(cursor, num_entries)
    print('users added')
    addFakeJobSalesDetails(cursor)
    print('Job Sales details added')
    CalculateNumJobsForRandClients(connector)
