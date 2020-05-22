from pandas import DataFrame


def printAnyFullTable(cursor, table_name):
    # DeletedAt in Client, Contacts, Users
    list_tables_with_DeletedAt = ['Client', 'Contacts', 'Users']
    select_query = "SELECT * FROM " + table_name
    if table_name in list_tables_with_DeletedAt:
        if table_name == 'Client':
            select_query = 'SELECT * FROM ClientView'
        elif table_name == 'Contacts':
            select_query = 'SELECT * FROM ContactView'
        elif table_name == 'Users':
            select_query = 'SELECT * FROM UserView'
    cursor.execute(select_query)
    result = cursor.fetchall()
    row_count = cursor.rowcount
    any_column_names = [i[0] for i in cursor.description]
    df = DataFrame(result,
                   columns=any_column_names)
    print(df.to_string(index=False))  # remove row indexing on pandas DataFrame
    # print(query)
    return row_count


def printClientTable(cursor):
    table_name = 'Client'
    printAnyFullTable(cursor, table_name)


def printJobTable(cursor):
    table_name = 'Job'
    printAnyFullTable(cursor, table_name)


def printCompanyCategoryTableLookup(cursor):
    table_name = 'CompanyCategoryTableLookup'
    printAnyFullTable(cursor, table_name)


def printResultTable(cursor):
    result = cursor.fetchall()
    any_column_names = [i[0] for i in cursor.description]
    df = DataFrame(result,
                   columns=any_column_names)
    print(df.to_string(index=False))  # remove row indexing on pandas DataFrame
    # print(query)


def printJobCostCalculatedTable(cursor):
    select_query = "SELECT JobCost_ID, Job_ID, MaterialsCost, Additions, ROUND(MaterialsCost + Additions, 2) AS Total_Cost FROM JobCost"
    cursor.execute(select_query)
    result = cursor.fetchall()
    any_column_names = [i[0] for i in cursor.description]
    df = DataFrame(result,
                   columns=any_column_names)
    print(df.to_string(index=False))  # remove row indexing on pandas DataFrame
    # print(query)

def avgJobCost(cursor):
    select_query = 'SELECT ROUND(AVG(MaterialsCost + Additions), 2) AS TotalCostAvg ' \
                   'FROM JobCost'
    cursor.execute(select_query)
    printResultTable(cursor)

def avgJobCostGreater(cursor):
    select_query = 'SELECT Job_ID, ROUND(MaterialsCost + Additions, 2) AS TotalCost FROM JobCost WHERE ( (MaterialsCost + Additions) > (SELECT SUM(MaterialsCost + Additions) DIV (SELECT Job_ID FROM JobCost ORDER BY Job_ID DESC LIMIT 1 ) AS Average_Total FROM JobCost));'
    cursor.execute(select_query)
    printResultTable(cursor)

def avgJobCostLesser(cursor):
    select_query = 'SELECT Job_ID, ROUND(MaterialsCost + Additions, 2) AS TotalCost FROM JobCost WHERE ( (MaterialsCost + Additions) < (SELECT SUM(MaterialsCost + Additions) DIV (SELECT Job_ID FROM JobCost ORDER BY Job_ID DESC LIMIT 1 ) AS Average_Total FROM JobCost));'
    cursor.execute(select_query)
    printResultTable(cursor)