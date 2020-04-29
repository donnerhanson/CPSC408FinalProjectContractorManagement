import csv
import random

import pandas as pd
from faker import Faker


def generateStringFloat(min_val, max_val, dec_places):
    return str(round(random.uniform(min_val, max_val), dec_places))


# this is for the main project testing
def exportDataBaseToCSV(mycursor):
    table_names_drop_order = ('JobSalesDetails', 'JobStatus', 'JobSubDetails', 'JobCost',
                              'Job', 'Contacts', 'Client', 'Users', 'StatusDefinition',
                              'CompanyCategoryTableLookup', 'Roles')
    fp = open('ContractorManagement.csv', 'w')
    for table in table_names_drop_order:
        query = "SELECT * FROM " + table
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        column_names = [i[0] for i in mycursor.description]
        tbl_list = [table]  # convert to list so output as a single entry on the newest line
        my_file = csv.writer(fp, lineterminator='\n')  # fp is file path
        my_file.writerow(tbl_list)
        my_file.writerow(column_names)
        my_file.writerows(myresult)
    fp.close()


table_names_add_order = ['Roles', 'CompanyCategoryTableLookup', 'StatusDefinition',
                         'Users', "Client", 'Contacts', 'Job', 'JobCost',
                         'JobSubDetails', "JobStatus", 'JobSalesDetails']


#################################################################
#  THIS IS THE RANDOM CSV GENERATION FUNCTION FOR ASSIGNMENT 3
################################################################
# 1 giant row for all tables pertaining to each job record
#


def exportFakeDataToCSV(file_name, num_entries):
    fp = open(file_name, 'w')
    # want output in each to be ([tableName], [headers], [data, '\n', data...])
    my_file = csv.writer(fp, lineterminator='\n')  # fp is file path
    i = 0
    while i < num_entries:
        my_file.writerow(addFakeEntryToCSV(i + 1, num_entries, round(num_entries / 3)))
        i += 1

    fp.close()


def addFakeEntryToCSV(job_id_num, max_contacts, sales_contacts):
    fake = Faker()
    # args = ([('name', 'address', 'city', 'state', 'email', 'phone')])
    # for x in range(0, num_entries):
    #    args.append((fake.name(), fake.street_address(), fake.city(), fake.state_abbr(), fake.postcode(),
    #                 fake.email(), fake.phone_number()))
    # args = (addFakeClientsToCSV(), addFakeCompanyCategoryIDToCSV(), addFakeRolesToCSV())
    # clients, catID, RolesTableNames, StatDef of Job, Job, Cost, StatusDefinitionTable,
    # Users, Contacts,
    # SubDetails, SalesDetails
    randStatusNum = addRandFakeStatusToCSV()[1]
    randStatusName = getStatusList()[randStatusNum]
    args = (fake.name(), fake.street_address(), fake.city(), fake.state_abbr(), fake.postcode(),
            fake.email(), fake.phone_number(),
            addFakeCompanyCategoryIDTableToCSV()[0], addFakeCompanyCategoryIDTableToCSV()[1],
            addFakeCompanyCategoryIDTableToCSV()[2], addFakeCompanyCategoryIDTableToCSV()[3],
            getRolesTable()[0], getRolesTable()[1], getRolesTable()[2], getRolesTable()[3],
            randStatusName,
            addFakeFloat(), addFakeFloat(), AddFakeHours(), AddFakeDate(),
            addFakeFloat(), addFakeFloat(),
            getStatusList()[0], getStatusList()[1],
            getStatusList()[2], getStatusList()[3],
            getStatusList()[4], getStatusList()[5],
            getStatusList()[6], getStatusList()[7],
            getStatusList()[8], getStatusList()[9],
            addFakeRolesIDToRow(),
            DateOrNull(),
            fake.name(), fake.url(), fake.email(), fake.phone_number(), addFakeCompanyCategoryIDToCSV(), 0,
            DateOrNull(),
            getRandomJobID(job_id_num), getRandomContactID(max_contacts), getRandomSalesID(sales_contacts), job_id_num,
            DateOrNull(), randStatusNum
            )
    # print(args)
    return args


def getRandomJobID(max_job_id):  # allows duplicate job ids to sub contractors
    return random.randint(1, max_job_id)


def getRandomContactID(max_contact_id):  # allows duplicate job ids to sub contractors
    return random.randint(1, max_contact_id)


def getRandomSalesID(max_sales_id):  # allows duplicate job ids to sub contractors
    return random.randint(1, max_sales_id)


def addFakeClientsToCSV():
    fake = Faker()
    args = [fake.name(), fake.street_address(), fake.city(), fake.state_abbr(), fake.postcode(),
            fake.email(), fake.phone_number()]
    return args


def DateOrNull():
    fake = Faker()
    x = random.randint(0, 1)
    if x == 0:
        return None
    else:
        return fake.date_time_this_decade(True)


# edit this
def addFakeRolesIDToRow():
    x = random.randint(0, 4)
    if x == 0:
        arg = 1
    elif x == 1:
        arg = 2
    elif x == 2:
        arg = 3
    else:
        arg = 4
    return arg


def getRolesTable():
    return ['Sales', 'Finance', 'Marketing', 'Owner']


# edit this
def addFakeCompanyCategoryIDTableToCSV():
    return ['Plumbing', 'Carpentry', 'Electric', 'Roofing']


def addFakeCompanyCategoryIDToCSV():
    return random.randint(0, 4)


# edit
def addRandFakeStatusToCSV():
    statuses = getStatusList()
    # 0,2,4,6,8,10
    # create a string then split the pairs to be passed as values to the db call
    random_number = random.randint(0, 10)
    if (random_number % 2) != 0:
        random_number += 1
    return statuses[random_number], random_number


def getStatusList():
    return ['Lead', 'Client has made contact with Company regarding job',
            'Accepted', 'Terms have been negotiated and contract signed',
            'Declined', 'Negotiations did not succeed - job not accepted',
            'Cancelled', 'Job has been permanently cancelled',
            'Postponed', 'Job has been postponed due to some type of emergency',
            'Finished', 'Job has been completed']


def addFakeFloat():
    return generateStringFloat(0.00, 9999.99, 2)


def AddFakeHours():
    return generateStringFloat(0.00, 20.99, 2)


def AddFakeDate():
    fake = Faker()
    return fake.date_time_this_decade(True)

