from datetime import datetime

from Messages import *
import mysql.connector.connection
import mysql.connector.cursor

from updateTable import RecordExists


def SoftDelete(connector):
    userChoice = -1
    while not (0 <= userChoice <= 2):
        userChoice = int(input(restore_or_delete_prompt))
        if userChoice == 1:  # delete
            DeleteOrRestoreClient(connector, userChoice)
        elif userChoice == 2:  # Restore
            DeleteOrRestoreClient(connector, userChoice)
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


def GetClientIDbyID(connector):
    ID = int(input(clientIDprompt))
    table = 'Client'
    conditionCategory = 'Client_ID'
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


def RestorePersonByID(connector, table, str_column, date_time, conditionCategory, ID):
    c = connector.cursor()
    query = """UPDATE %s SET %s = %s WHERE (%s = %s)""" % (
        table, str_column, date_time, conditionCategory, ID)
    c.execute(query, )
    connector.commit()
    return
