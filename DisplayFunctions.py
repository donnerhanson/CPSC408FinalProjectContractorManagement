from pandas import DataFrame


def printAnyFullTable(cursor, table_name):
    # DeletedAt in Client, Contacts, Users
    list_tables_with_DeletedAt = ['Client', 'Contacts', 'Users']
    select_query = "SELECT * FROM " + table_name
    if table_name in list_tables_with_DeletedAt:
        select_query += " WHERE DeletedAt IS NULL"
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
    select_query = "SELECT JobCost_ID, Job_ID, MaterialsCost, Additions, (MaterialsCost + Additions) AS Total_Cost FROM JobCost"
    cursor.execute(select_query)
    result = cursor.fetchall()
    any_column_names = [i[0] for i in cursor.description]
    df = DataFrame(result,
                   columns=any_column_names)
    print(df.to_string(index=False))  # remove row indexing on pandas DataFrame
    # print(query)

def avgJobCost(cursor):
    select_query = 'SELECT AVG(ROUND(MaterialsCost + Additions, 2)) AS TotalCostAvg ' \
                   'FROM JobCost'
    cursor.execute(select_query)
    printResultTable(cursor)
