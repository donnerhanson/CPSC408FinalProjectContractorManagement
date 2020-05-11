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
    if delOrRestore == 1:
        while confirm not in options:
            confirm = str(input(delete_confirmation))
            confirm = confirm.lower()
        if confirm == 'y':
            ID = GetClientIDbyID(connector)
            if ID == 0:
                return 0
            delete_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # connector, table, col_name, update_to_value, col_name_condition, condition_in
            UpdateRowByOneCondition(connector, table, col_name, delete_date, condition, ID)
        elif confirm == 'n':
            return 0
        else:
            return 0
    elif delOrRestore == 2:
        while confirm.lower() not in options:
            confirm = str(input(delete_confirmation))
            confirm = confirm.lower()
        if confirm == 'y':
            ID = GetClientIDbyID(connector)
            delete_date = None
            # connector, table, col_name, update_to_value, col_name_condition, condition_in
            UpdateRowByOneCondition(connector, table, col_name, delete_date, condition, ID)
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
    query = """UPDATE %s SET %s = '%s' WHERE %s = '%s'""" % (table, col_name, update_to_value, col_name_condition, condition_in)
    somevar = 0
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