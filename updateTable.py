import mysql.connector
from DisplayFunctions import printResultTable
from Messages import *
import re

update_table_prompt = '1: To update Client Information\n' \
                      '2: To update Job/Job Cost...\n' \
                      '3: To update Contact Information...\n' \
                      '4: To update User (Employee Information)\n'


def UpdateTable(connector, table_choice):
    if table_choice == 1:
        UpdateClient(connector)
    elif table_choice == 2:
        something = 0
    elif table_choice == 3:
        something = 0
    elif table_choice == 4:
        something = 0
    else:
        return
    return


update_client_search_options = 'If searched client does not exist this current\n' \
                               'process will exit without changes to the system...\n' \
                               '1: Find Client by ID\n' \
                               '2: Find Client by Name\n' \
                               '3: Find Client by email\n' \
                               '0: Exit Update Process...'

update_client_options = '1: Update Name\n' \
                        '2: Update Street Address\n' \
                        '3: Update City\n' \
                        '4: Update State\n' \
                        '5: Update Zip Code\n' \
                        '6: Update Email\n' \
                        '7: Update Phone Number\n' \
                        '0: Exit Update...\n'


# clientIDprompt
# addressInMessage
# cityInMessage
# stateInMessage
# zipInMessage
# phoneInMessage
# emailInMessage
# TODO: UPDATE BY ID FUNCTIONING
def UpdateClientAttributes(connector, table, conditionCategory, condition):
    c = connector.cursor()
    data = (table, conditionCategory, condition)
    if conditionCategory in ('ClientName', 'Email'): # force ID lookup
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
            query = """UPDATE %s SET %s = '%s' WHERE (%s = '%s')""" % (table, str_column, update_value, conditionCategory, condition)
            c.execute(query, )
            connector.commit()
        c.execute(select_query, )
        printResultTable(c)
        userChoice = int(input(update_client_options))
    return 0


def UpdateClient(connector):
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

        if categoryCondition in 'Client_ID' and RecordExists(connector, curr_table_name, str(categoryCondition), searched_value):
            # connector, table, conditionCategory, condition
            userChoice = UpdateClientAttributes(connector, curr_table_name, categoryCondition, searched_value)
        elif categoryCondition in ('ClientName', 'Email') and RecordExistsLike(connector, curr_table_name,  str(categoryCondition), searched_value):
            userChoice = UpdateClientAttributes(connector, curr_table_name, categoryCondition, searched_value)
        else:
            print('record does not exist')
    return


def RecordExists(connector, table, conditionCategory, condition):
    cursor = connector.cursor()
    data = (table, conditionCategory, condition)
    query = """SELECT COUNT(*) FROM %s WHERE %s = '%s'""" % (data[0], data[1], data[2])
    cursor.execute(query, )
    results = cursor.fetchall()
    # gets the number of rows affected by the command executed
    row_count = cursor.rowcount
    print("Number of similar rows: {}...\n".format(row_count))
    if row_count == 0:
        return False
    if row_count > 1:
        print("multiple matching records please use another method to update...\n")
        return False
    return True


def RecordExistsLike(connector, table, conditionCategory, condition):
    cursor = connector.cursor()
    data = (table, conditionCategory, condition)
    query = """SELECT Client_ID FROM %s WHERE %s LIKE '%s'""" % (data[0], data[1], "%" + data[2] + "%")
    cursor.execute(query, )
    results = cursor.fetchall()
    # gets the number of rows affected by the command executed
    row_count = cursor.rowcount
    print("Number of similar rows: {}...\n".format(row_count))
    if row_count == 0:
        return False
    if row_count > 1:
        print("multiple matching records please use another method to update...\n")
        return False
    return True
