import csv
import random

from faker import Faker

table_names_drop_order = ['JobSalesDetails', 'JobStatus', 'JobSubDetails', 'JobCost',
                          'Job', 'Contacts', 'Client', 'Users', 'StatusDefinition',
                          'CompanyCategoryTableLookup', 'Roles']


#def exportFakeDataToCSV(file_name, num_entries, dataHandler: csvHandler):
 #   dataHandler(file_name, num_entries)
  #  print(dataHandler.addFakeClientsToCSV(5))

   # fp = open(file_name, 'w')

    # want output in each to be ([tableName], [headers], [data, '\n', data...])

    #column_names = [i[0] for i in mycursor.description]
    #tbl_list = [table_names_drop_order]  # convert to list so output as a single entry on the newest line
    #my_file = csv.writer(fp, lineterminator='\n')  # fp is file path
    #my_file.writerow(tbl_list)
    #my_file.writerow(column_names)
    #my_file.writerows(myresult)
    #fp.close()


def exportDataBaseToCSV(mycursor):
    fp = open('ContractorManagement.csv', 'w')
    for table in table_names_drop_order:
        # print(table)
        query = "SELECT * FROM " + table
        # print(query)
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        column_names = [i[0] for i in mycursor.description]
        tbl_list = [table]  # convert to list so output as a single entry on the newest line
        my_file = csv.writer(fp, lineterminator='\n')  # fp is file path
        my_file.writerow(tbl_list)
        my_file.writerow(column_names)
        my_file.writerows(myresult)
    fp.close()


def generateStringFloat(min, max, dec_places):
    return str(round(random.uniform(min, max), dec_places))


def addFakeClientsToDB(cursor, num_entries):
    fake = Faker()
    for x in range(0, num_entries):
        args = [fake.name(), fake.street_address(), fake.city(), fake.state_abbr(), fake.postcode(),
                fake.email(), fake.phone_number()]
        cursor.callproc('AddClient', args)


def addFakeRolesToDB(cursor):
    for x in range(0, 3):
        if x == 0:
            arg = ['Sales']
        elif x == 1:
            arg = ['Finance']
        elif x == 2:
            arg = ['Marketing']
        else:
            arg = ['Owner']
        cursor.callproc('CreateRole', arg)


def addFakeCompanyCategoryIDToDB(cursor):
    for x in range(0, 4):
        if x == 0:
            arg = ['Plumbing']
        elif x == 1:
            arg = ['Carpentry']
        elif x == 2:
            arg = ['Electric']
        elif x == 3:
            arg = ['Roofing']
        else:
            arg = ['Painting']
        cursor.callproc('CreateCompanyCategoryID', arg)


def addFakeStatusDefinitionToDB(cursor, num_entries):
    statuses = ['Lead', 'Client has made contact with Company regarding job',
                'Accepted', 'Terms have been negotiated and contract signed',
                'Declined', 'Negotiations did not succeed - job not accepted',
                'Cancelled', 'Job has been permanently cancelled',
                'Postponed', 'Job has been postponed due to some type of emergency',
                'Finished', 'Job has been completed']
    is_pair = False
    # create a string then split the pairs to be passed as values to the db call
    for i in statuses:
        if not is_pair:
            args = i
            is_pair = True
        else:
            args += (',' + i)
            is_pair = False
            new_args = args.split(',')
            cursor.callproc('CreateStatusDefinition', new_args)
    return


def addFakeJobCostToDB(cursor):
    cursor.execute("select JOBCost_ID from JobCost ORDER BY JOBCost_ID DESC LIMIT 1")
    lastJobIDList = cursor.fetchall()  # returns a list with a tuple inside
    lastJobID = 0
    for value in lastJobIDList:  # iterate the list
        for num in value:  # iterate the tuple
            if num > 0:
                lastJobID = num
                break
            elif num is None:
                print('no jobs available')
            else:
                print('something happened')
    # print(lastJobID)
    i = 0
    while i < int(lastJobID):
        i += 1
        # print(i)
        Mats = generateStringFloat(0.00, 9999.99, 2)
        adds = generateStringFloat(0.00, 9999.99, 2)
        # print(Mats)
        # print(adds)
        args = (i, Mats, adds)
        cursor.callproc('UpdateJobCost', args)
    # select_query = "SELECT * FROM JobCost"
    # cursor.execute(select_query)
    return


def addFakeJobToDB(cursor):
    fake = Faker()
    #"AddJob(IN ClientIDIn int, IN EstimateIn float, IN PayoutIn float, IN HoursIN float,IN DateIN datetime)"
    cursor.execute("select Client_ID from Client ORDER BY Client_ID DESC LIMIT 1")  # get last Client
    lastClientIDList = cursor.fetchall()  # returns a list with a tuple inside
    lastClientID = 0
    for value in lastClientIDList:  # iterate the list
        for num in value:  # iterate the tuple
            if num > 0:
                lastClientID = num
                break
            elif num is None:
                print('no jobs available')
            else:
                print('something happened')
    clientID = 0
    while clientID < int(lastClientID):
        clientID += 1
        Estimate = generateStringFloat(0.00, 9999.99, 2)
        Payout = generateStringFloat(0.00, 9999.99, 2)
        Hours = generateStringFloat(0.00, 20.99, 2)
        date = fake.date_time_this_decade(True)
        # print(Mats)
        # print(adds)
        args = (clientID, Estimate, Payout, Hours, date)
        cursor.callproc('AddJob', args)
    return


def addFakeContact():
    return


def addFakeJobSubDetails():
    return

def addFakeUsers(cursor):
    fake = Faker()
    cursor.execute("SELECT Role_ID FROM Roles ORDER BY Role_ID DESC LIMIT 1")
    lastRoleIDList = cursor.fetchall()
    lastRoleID = 0
    for value in lastRoleIDList:
        for num in value:
            if num > 0:
                lastRoleID = num
                break
            elif num is None:
                print('No users')
            else:
                print('Error')
    roleID = 0
    while roleID < int(lastRoleID):
        roleID += 1
    args = fake.name(), roleID, fake.street_address(), fake.city(), fake.state_abbr(), fake.postcode(),
    fake.phone_number(), fake.email()
    cursor.callproc('CreateUser', args)
    return
