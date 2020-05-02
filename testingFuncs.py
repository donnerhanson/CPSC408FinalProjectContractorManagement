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
    print('Company Category Table Lookup added')
    addFakeStatusDefinitionToDB(cursor, num_entries)  # done
    # printAnyTable(cursor, tableNamesAddOrder[2])
    print('Status Definitions added')
    addFakeJobToDB(cursor)  # Links to all available clients
    print('Jobs Added')
    addFakeJobCostToDB(cursor)  # links to all available jobs
    print('Job Cost added')
    addFakeContacts(cursor, num_entries)
    print('Contacts added')
    addFakeJobSubDetails(cursor)
    print('Job Sub Details added')
    addFakeUsers(cursor, num_entries)
    print('Users added')
    addFakeJobSalesDetails(cursor)
    print('Job Sales details added')
    CalculateNumJobsForRandClients(connector)
