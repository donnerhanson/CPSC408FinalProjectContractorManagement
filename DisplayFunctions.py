from pandas import DataFrame


def printAnyFullTable(cursor, table_name):
    select_query = "SELECT * FROM " + table_name
    cursor.execute(select_query)
    result = cursor.fetchall()
    any_column_names = [i[0] for i in cursor.description]
    df = DataFrame(result,
                   columns=any_column_names)
    print(df.to_string(index=False))  # remove row indexing on pandas DataFrame
    # print(query)


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

