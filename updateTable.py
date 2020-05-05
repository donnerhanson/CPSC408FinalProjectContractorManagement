import mysql.connector
from Messages import *


# update_table_prompt = '1: To update Client Information\n' \
#                            '2: To update Job/Job Cost...\n' \
#                            '3: To update Contact Information...\n' \
#                            '4: To update User (Employee Information)'

def UpdateTable(connector, table_choice):
    if table_choice == 1:
        something = 0
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
                               '3: Find Client by email...\n'

update_client_options = '1: Update Name:\n' \
                        '2: Update Street Address:\n' \
                        '3: Update City\n' \
                        '4: Update State\n' \
                        '5: Update Zip Code\n' \
                        '6: Update Email\n' \
                        '7: Update Phone Number\n' \
                        '0: Exit Update'


# clientIDprompt
# addressInMessage
# cityInMessage
# stateInMessage
# zipInMessage
# phoneInMessage
# emailInMessage
# TODO
def UpdateClientAttributes(connector, table, conditionCategory, condition):
    userChoice = int(input(update_client_options))
    c = connector.cursor()
    while userChoice != 0:
        if userChoice == 1:  # name
            name = input(clientInName)
            continue
        elif userChoice == 2:  # address
            address = input(addressInMessage)
            continue
        elif userChoice == 3:  # city
            city = input(cityInMessage)
            continue
        elif userChoice == 4:  # state
            state = input(stateInMessage)
            continue
        elif userChoice == 5:  # zip
            zip_code = input(zipInMessage)
            continue
        elif userChoice == 6:  # email
            email = input(emailInMessage)
            continue
        elif userChoice == 7:  # phone
            phone = input(phoneInMessage)
            continue
        else:
            continue
        userChoice = int(input(update_client_options))
    return


def UpdateClient(connector):
    c = connector.cursor()
    userChoice = int(input(update_client_search_options))
    curr_table_name = 'Client'
    categoryCondition = ''
    if userChoice == 1:  # ID
        userChoice = int(input(clientIDprompt))
        categoryCondition = 'Client_ID'
        if RecordExists(c, curr_table_name, categoryCondition, userChoice):
            UpdateClientAttributes()
    elif userChoice == 2:  # name
        something = 0
    elif userChoice == 3:  # email
        something = 0
    else:
        return
    return


def RecordExists(cursor, table, conditionCategory, condition):
    cursor.execute(
        "SELECT COUNT(*) FROM %s WHERE %s = %s",
        (table, conditionCategory, condition,)
    )
    results = cursor.fetchall()
    # gets the number of rows affected by the command executed
    row_count = cursor.rowcount
    print("Number of similar rows: {}...".format(row_count))
    if row_count == 0:
        return False
    if row_count > 1:
        print("multiple matching records please use another method to update...\n")
        return False
    return True
