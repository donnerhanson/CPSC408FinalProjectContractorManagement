import mysql.connector
from datetime import datetime
from DisplayFunctions import printResultTable
from Messages import *
from userInput import *
import re

from dateFuncs import getDate, timedelta


def UpdateTable(connector, table_choice):
    if table_choice == 1:
        GetClientRecord(connector)
    elif table_choice == 2:
        GetJobRecord(connector)
    elif table_choice == 3:
        GetContactRecord(connector)
    elif table_choice == 4:
        UpdateUser(connector)
    else:
        return
    return


# client options
update_client_search_options = 'If searched client does not exist this current\n' \
                               'process will exit without changes to the system...\n' \
                               '1: Find Client by ID\n' \
                               '2: Find Client by Name\n' \
                               '3: Find Client by email\n' \
                               '0: Exit Update Process...\n'

update_client_options = '1: Update Name\n' \
                        '2: Update Street Address\n' \
                        '3: Update City\n' \
                        '4: Update State\n' \
                        '5: Update Zip Code\n' \
                        '6: Update Email\n' \
                        '7: Update Phone Number\n' \
                        '0: Exit Update...\n'

# contact options
update_contact_search_options = 'If searched contact does not exist this current\n' \
                                'process will exit without changes to the system...\n' \
                                '1: Find Contact by ID\n' \
                                '2: Find Contact by Name\n' \
                                '3: Find Contact by email\n' \
                                '0: Exit Update Process...\n'

update_contact_options = '1: Update Name\n' \
                         '2: Update URL\n' \
                         '3: Update Email\n' \
                         '4: Update Phone Number\n' \
                         '0: Exit Update...\n'

# user options
update_user_search_options = 'If searched contact does not exist this current\n' \
                                'process will exit without changes to the system...\n' \
                                '1: Find User by ID\n' \
                                '2: Find User by Name\n' \
                                '3: Find User by email\n' \
                                '0: Exit Update Process...\n'

update_user_options = '1: Update Name\n' \
                        '2: Update Role\n' \
                        '3: Update Street Address\n' \
                        '4: Update City\n' \
                        '5: Update State\n' \
                        '6: Update Zip Code\n' \
                        '7: Update Phone Number\n' \
                        '8: Update Email\n' \
                        '0: Exit Update...\n'


# clientIDprompt
# addressInMessage
# cityInMessage
# stateInMessage
# zipInMessage
# phoneInMessage
# emailInMessage
# TODO: UPDATE BY ID FUNCTIONING


# ATTRIBUTE UPDATES
def UpdateClientAttributes(connector, table, conditionCategory, condition):
    c = connector.cursor()
    data = (table, conditionCategory, condition)
    if conditionCategory in ('ClientName', 'Email'):  # force ID lookup
        select_query = """SELECT Client_ID FROM %s WHERE %s LIKE '%s'""" % (data[0], data[1], "%" + str(data[2]) + "%")
        c.execute(select_query, )
        result = c.fetchall()
        for i in result:
            for j in i:
                if j >= 1:
                    condition = j
        conditionCategory = 'Client_ID'
        data = (table, conditionCategory, condition)

    select_query = """SELECT * FROM %s WHERE %s = %s""" % (data[0], data[1], str(data[2]))
    c.execute(select_query, )
    printResultTable(c)
    userChoice = int(input(update_client_options))
    while userChoice != 0:
        update_value = ''
        column = ''
        if userChoice == 1:  # name
            update_value = input(clientInName)
            column = 'ClientName'
        elif userChoice == 2:  # address
            update_value = input(addressInMessage)
            column = 'Address'
        elif userChoice == 3:  # city
            update_value = input(cityInMessage)
            column = 'City'
        elif userChoice == 4:  # state
            update_value = input(stateInMessage)
            if len(update_value) != 2 or re.search('[0-9]', update_value):
                print('Error: State Values are accepted in format: \'CA\'')
            else:
                column = 'State'
        elif userChoice == 5:  # zip
            update_value = input(zipInMessage)
            if len(update_value) != 5 or re.search('[a-zA-Z]', update_value):
                print("Error: zip code is 5 integers ex: 55555...\n")
            else:
                column = 'Zip'
        elif userChoice == 6:  # email
            update_value = input(emailInMessage)
            column = 'Email'
        elif userChoice == 7:  # phone
            update_value = input(phoneInMessage)
            column = 'Phone'
        str_column = str(column)
        if column != '':
            query = """UPDATE %s SET %s = '%s' WHERE (%s = '%s')""" % (
                table, str_column, update_value, conditionCategory, condition)
            c.execute(query, )
            connector.commit()
        c.execute(select_query, )
        printResultTable(c)
        userChoice = int(input(update_client_options))
    return 0


def UpdateContactAttributes(connector, table, conditionCategory, condition):
    c = connector.cursor()
    data = (table, conditionCategory, condition)
    if conditionCategory in ('ContactName', 'Email'):  # force ID lookup
        select_query = """SELECT Contact_ID FROM %s WHERE %s LIKE '%s'""" % (data[0], data[1], "%" + str(data[2]) + "%")
        c.execute(select_query, )
        result = c.fetchall()
        for i in result:
            for j in i:
                if j >= 1:
                    condition = j
        conditionCategory = 'Contact_ID'
        data = (table, conditionCategory, condition)

    select_query = """SELECT * FROM %s WHERE %s = %s""" % (data[0], data[1], str(data[2]))
    c.execute(select_query, )
    printResultTable(c)
    userChoice = int(input(update_contact_options))
    while userChoice != 0:
        update_value = ''
        column = ''
        if userChoice == 1:  # name
            update_value = input(contactInName)
            column = 'ContactName'
        elif userChoice == 2:  # url
            update_value = input(contactInURL)
            column = 'URL'
        elif userChoice == 3:  # email
            update_value = input(emailInMessage)
            column = 'Email'
        elif userChoice == 4:  # phone
            update_value = input(phoneInMessage)
            column = 'Phone'
        str_column = str(column)
        if column != '':
            query = """UPDATE %s SET %s = '%s' WHERE (%s = '%s')""" % (
                table, str_column, update_value, conditionCategory, condition)
            c.execute(query, )
            connector.commit()
        c.execute(select_query, )
        printResultTable(c)
        userChoice = int(input(update_contact_options))
    return 0

def UpdateUserAttributes(connector, table, conditionCategory, condition):
    c = connector.cursor()
    data = (table, conditionCategory, condition)
    if conditionCategory in ('Name', 'Email'):  # force ID lookup
        select_query = """SELECT User_ID FROM %s WHERE %s LIKE '%s'""" % (data[0], data[1], "%" + str(data[2]) + "%")
        c.execute(select_query, )
        result = c.fetchall()
        for i in result:
            for j in i:
                if j >= 1:
                    condition = j
        conditionCategory = 'User_ID'
        data = (table, conditionCategory, condition)

    select_query = """SELECT * FROM %s WHERE %s = %s""" % (data[0], data[1], str(data[2]))
    c.execute(select_query, )
    printResultTable(c)
    userChoice = int(input(update_user_options))
    while userChoice != 0:
        update_value = ''
        column = ''
        if userChoice == 1:  # name
            update_value = input(userInName)
            column = 'Name'
        elif userChoice == 2: #role ID
            update_value = input(userRoleIDIn)
            column = 'Role_ID'
        elif userChoice == 3:  # address
            update_value = input(addressInMessage)
            column = 'Address'
        elif userChoice == 4:  # city
            update_value = input(cityInMessage)
            column = 'City'
        elif userChoice == 5:  # state
            update_value = input(stateInMessage)
            if len(update_value) != 2 or re.search('[0-9]', update_value):
                print('Error: State Values are accepted in format: \'CA\'')
            else:
                column = 'State'
        elif userChoice == 6:  # zip
            update_value = input(zipInMessage)
            if len(update_value) != 5 or re.search('[a-zA-Z]', update_value):
                print("Error: zip code is 5 integers ex: 55555...\n")
            else:
                column = 'Zip'
        elif userChoice == 7:  # phone
            update_value = input(phoneInMessage)
            column = 'Phone'
        elif userChoice == 8:  # email
            update_value = input(emailInMessage)
            column = 'Email'
        str_column = str(column)
        if column != '':
            query = """UPDATE %s SET %s = '%s' WHERE (%s = '%s')""" % (
            table, str_column, update_value, conditionCategory, condition)
            c.execute(query, )
            connector.commit()
        c.execute(select_query, )
        printResultTable(c)
        userChoice = int(input(update_user_options))
    return 0


# GET SINGLE RECORD
def GetClientRecord(connector):
    userChoice = int(input(update_client_search_options))
    curr_table_name = 'Client'
    while int(userChoice) != 0:
        categoryCondition = ''
        searched_value = ''
        if userChoice == 1:  # ID
            searched_value = int(input(clientIDprompt))
            categoryCondition = 'Client_ID'
        elif userChoice == 2:  # name
            searched_value = input("enter client name...\n")
            categoryCondition = 'ClientName'
        elif userChoice == 3:  # email
            searched_value = input("enter client email...\n")
            categoryCondition = 'Email'

        if categoryCondition in 'Client_ID' and RecordExists(connector, curr_table_name, str(categoryCondition),
                                                             searched_value):
            # connector, table, conditionCategory, condition
            userChoice = UpdateClientAttributes(connector, curr_table_name, categoryCondition, searched_value)
        elif categoryCondition in ('ClientName', 'Email') and RecordExistsLike(connector, curr_table_name,
                                                                               str(categoryCondition), searched_value):
            userChoice = UpdateClientAttributes(connector, curr_table_name, categoryCondition, searched_value)
        else:
            userChoice = int(input(update_client_search_options))
    return


def GetJobRecord(connector):
    userChoice = int(input(update_job_search_options))
    curr_table_name = 'Job'
    while int(userChoice) != 0:
        categoryCondition = ''
        searched_value = ''
        if userChoice == 1:  # ID
            searched_value = int(input(jobIDPrompt))
            categoryCondition = 'Job_ID'
        elif userChoice == 2:  # name
            searched_value = input(clientIDprompt)
            categoryCondition = 'Client_ID'
        elif userChoice == 3:  # Date
            searched_value = getDate()
            # searched_value = searched_value
            categoryCondition = 'Last_active'

        if categoryCondition in ('Job_ID', 'Client_ID') and RecordExists(connector, curr_table_name,
                                                                         str(categoryCondition),
                                                                         searched_value):
            # connector, table, conditionCategory, condition
            userChoice = UpdateContactAttributes(connector, curr_table_name, categoryCondition, searched_value)
        elif categoryCondition in 'Last_active' and RecordExistsDate(connector, curr_table_name,
                                                              str(categoryCondition), searched_value):
            userChoice = UpdateContactAttributes(connector, curr_table_name, categoryCondition, searched_value)
        else:
            userChoice = int(input(update_job_search_options))
    return


def GetContactRecord(connector):
    userChoice = int(input(update_contact_search_options))
    curr_table_name = 'Contacts'
    while int(userChoice) != 0:
        categoryCondition = ''
        searched_value = ''
        if userChoice == 1:  # ID
            searched_value = int(input(contactIDprompt))
            categoryCondition = 'Contact_ID'
        elif userChoice == 2:  # name
            searched_value = input(contactInName)
            categoryCondition = 'ContactName'
        elif userChoice == 3:  # email
            searched_value = input(contactInEmail)
            categoryCondition = 'Email'

        if categoryCondition in 'Contact_ID' and RecordExists(connector, curr_table_name, str(categoryCondition),
                                                              searched_value):
            # connector, table, conditionCategory, condition
            userChoice = UpdateContactAttributes(connector, curr_table_name, categoryCondition, searched_value)
        elif categoryCondition in ('ContactName', 'Email') and RecordExistsLike(connector, curr_table_name,
                                                                                str(categoryCondition), searched_value):
            userChoice = UpdateContactAttributes(connector, curr_table_name, categoryCondition, searched_value)
        else:
            userChoice = int(input(update_contact_search_options))
    return

def UpdateUser(connector):
    userChoice = int(input(update_user_search_options))
    curr_table_name = 'Users'
    while int(userChoice) != 0:
        categoryCondition = ''
        searched_value = ''
        if userChoice == 1:  # ID
            searched_value = int(input(userIDPrompt))
            categoryCondition = 'User_ID'
        elif userChoice == 2:  # name
            searched_value = input("enter user name...\n")
            categoryCondition = 'Name'
        elif userChoice == 3:  # email
            searched_value = input("enter user email...\n")
            categoryCondition = 'Email'

        if categoryCondition in 'User_ID' and RecordExists(connector, curr_table_name, str(categoryCondition),
                                                             searched_value):
            # connector, table, conditionCategory, condition
            userChoice = UpdateUserAttributes(connector, curr_table_name, categoryCondition, searched_value)
        elif categoryCondition in ('Name', 'Email') and RecordExistsLike(connector, curr_table_name,
                                                                               str(categoryCondition), searched_value):
            userChoice = UpdateUserAttributes(connector, curr_table_name, categoryCondition, searched_value)
        else:
            userChoice = int(input(update_user_search_options))
    return

def RecordExists(connector, table, conditionCategory, condition):
    cursor = connector.cursor()
    data = (table, conditionCategory, condition)
    query = """SELECT * FROM %s WHERE %s = '%s'""" % (data[0], data[1], data[2])
    cursor.execute(query, )
    results = cursor.fetchall()  # clears cursor results to allow for next query if needed
    # gets the number of rows affected by the command executed
    row_count = cursor.rowcount
    print("Number of similar rows, {}:\n".format(row_count))
    if row_count <= 0:
        print('record does not exist\n')
        return False
    if row_count > 1:
        print("multiple matching records please use another method to update...\n")
        return False
    return True


def RecordExistsLike(connector, table, conditionCategory, condition):
    cursor = connector.cursor()
    data = (table, conditionCategory, condition)
    query = """SELECT * FROM %s WHERE %s LIKE '%s'""" % (data[0], data[1], "%" + data[2] + "%")
    cursor.execute(query, )
    results = cursor.fetchall()
    # gets the number of rows affected by the command executed
    row_count = cursor.rowcount
    print("Number of similar rows, {}:\n".format(row_count))
    if row_count <= 0:
        print('record does not exist\n')
        return False
    if row_count > 1:
        print("multiple matching records please use another method to update...\n")
        return False
    return True


def RecordExistsDate(connector, table, conditionCategory, condition): #TODO: DATE NOT being accepted by query
    cursor = connector.cursor()
    data = (table, conditionCategory, condition)
    start_date = data[2].strftime('%Y-%m-%d')
    end_date = (data[2] + timedelta(days=1)).strftime('%Y-%m-%d')
    query = """SELECT * FROM %s WHERE %s BETWEEN ( %s AND %s )""" % (data[0], data[1], start_date, end_date)
    cursor.execute(query,)
    results = cursor.fetchall()
    # gets the number of rows affected by the command executed
    row_count = cursor.rowcount
    print("Number of similar rows, {}:\n".format(row_count))
    if row_count <= 0:
        print('record does not exist\n')
        return False
    if row_count > 1:
        print("multiple matching records please use another method to update...\n")
        return False
    return True
