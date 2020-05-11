from datetime import datetime

from Messages import *
import mysql.connector.connection
import mysql.connector.cursor

import re

from inputParseFuncs import is_only_nums
from updateTable import RecordExists


def SoftDelete(connector):
    userChoice = -1
    # all userChoice inputs eval in funcs at 1 = del and 2 = restore
    # therefore
    multiply_this_by_option_row = 2
    while not (0 <= userChoice <= 6):
        userChoice = input(restore_or_delete_prompt)
        if not is_only_nums(userChoice):
            userChoice = -1
        userChoice = int(userChoice)
        if userChoice == 1 or userChoice == 2:
            DeleteOrRestoreClient(connector, userChoice)
        elif userChoice == 3 or userChoice == 4:
            userChoice -= (1 * multiply_this_by_option_row)
            DeleteOrRestoreContact(connector, userChoice)
        elif userChoice == 5 or userChoice == 6:
            userChoice -= (2 * multiply_this_by_option_row)
            DeleteOrRestoreUser(connector, userChoice)
        elif userChoice == 0:
            break
    return


def DeleteOrRestoreClient(connector, delOrRestore):
    confirm = ''
    options = ('y', 'n')
    table = 'Client'
    condition = 'Client_ID'
    col_name = 'DeletedAt'
    ID = GetClientIDbyID(connector)
    if delOrRestore == 1 and ID != 0:
        while confirm not in options:
            confirm = str(input(delete_confirmation))
            confirm = confirm.lower()
        if confirm == 'y':
            if ID == 0:
                return 0
            delete_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # connector, table, col_name, update_to_value, col_name_condition, condition_in
            UpdateRowByOneCondition(connector, table, col_name, delete_date, condition, ID)
        elif confirm == 'n':
            return 0
        else:
            return 0
    elif delOrRestore == 2 and ID != 0:
        while confirm.lower() not in options:
            confirm = str(input(restore_confirmation))
            confirm = confirm.lower()
        if confirm == 'y':
            restore_date = None
            # connector, table, col_name, update_to_value, col_name_condition, condition_in
            UpdateRowByOneCondition(connector, table, col_name, restore_date, condition, ID)
        elif confirm == 'n':
            return 0
        else:
            return 0
    return 0


def DeleteOrRestoreContact(connector, delOrRestore):
    confirm = ''
    options = ('y', 'n')
    table = 'Contacts'
    condition = 'Contact_ID'
    col_name = 'DeletedAt'
    ID = GetContactIDbyID(connector)
    if delOrRestore == 1 and ID != 0:
        while confirm not in options:
            confirm = str(input(delete_confirmation))
            confirm = confirm.lower()
        if confirm == 'y':
            if ID == 0:
                return 0
            delete_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # connector, table, col_name, update_to_value, col_name_condition, condition_in
            UpdateRowByOneCondition(connector, table, col_name, delete_date, condition, ID)
        elif confirm == 'n':
            return 0
        else:
            return 0
    elif delOrRestore == 2 and ID != 0:
        while confirm.lower() not in options:
            confirm = str(input(restore_confirmation))
            confirm = confirm.lower()
        if confirm == 'y':
            restore_date = None
            # connector, table, col_name, update_to_value, col_name_condition, condition_in
            UpdateRowByOneCondition(connector, table, col_name, restore_date, condition, ID)
        elif confirm == 'n':
            return 0
        else:
            return 0
    return 0

def DeleteOrRestoreUser(connector, delOrRestore):
    confirm = ''
    options = ('y', 'n')
    table = 'Users'
    condition = 'User_ID'
    col_name = 'DeletedAt'
    ID = GetUserIDbyID(connector)
    if delOrRestore == 1 and ID != 0:
        while confirm not in options:
            confirm = str(input(delete_confirmation))
            confirm = confirm.lower()
        if confirm == 'y':
            if ID == 0:
                return 0
            delete_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # connector, table, col_name, update_to_value, col_name_condition, condition_in
            UpdateRowByOneCondition(connector, table, col_name, delete_date, condition, ID)
        elif confirm == 'n':
            return 0
        else:
            return 0
    elif delOrRestore == 2 and ID != 0:
        while confirm.lower() not in options:
            confirm = str(input(restore_confirmation))
            confirm = confirm.lower()
        if confirm == 'y':
            restore_date = None
            # connector, table, col_name, update_to_value, col_name_condition, condition_in
            UpdateRowByOneCondition(connector, table, col_name, restore_date, condition, ID)
        elif confirm == 'n':
            return 0
        else:
            return 0
    return 0

def GetClientIDbyID(connector):
    ID = int(input(clientIDprompt))
    table = 'Client'
    conditionCategory = 'Client_ID'
    if RecordExists(connector, table, conditionCategory, ID):
        return ID
    else:
        return 0


def GetContactIDbyID(connector):
    ID = int(input(contactIDprompt))
    table = 'Contacts'
    conditionCategory = 'Contact_ID'
    if RecordExists(connector, table, conditionCategory, ID):
        return ID
    else:
        return 0

def GetUserIDbyID(connector):
    ID = int(input(userIDPrompt))
    table = 'Users'
    conditionCategory = 'User_ID'
    if RecordExists(connector, table, conditionCategory, ID):
        return ID
    else:
        return 0

def UpdateRowByOneCondition(connector, table, col_name, update_to_value, col_name_condition, condition_in):
    c = connector.cursor()
    if update_to_value is None:  # most likely for setting date to null
        query = """UPDATE %s SET %s = NULL WHERE %s = '%s'""" % (
            table, col_name, col_name_condition, condition_in)
    else:
        query = """UPDATE %s SET %s = '%s' WHERE %s = '%s'""" % (
            table, col_name, update_to_value, col_name_condition, condition_in)
    c.execute(query, )
    connector.commit()
    return
