import csv

tableNamesAddOrder = ('Roles', 'CompanyCategoryTableLookup', 'StatusDefinition',
                      'Users', 'Client', 'Contacts', 'Job', 'JobCost',
                      'JobSubDetails', 'JobStatus', 'JobSalesDetails')


def importToDatabase(file_name, mycursor):
    i = 0

    datafile = open(file_name, 'r')
    myreader = csv.reader(datafile)
    # roles 11-14
    for row in myreader:
        # done in add table order

        # roles
        if i == 0:
            j = 11
            while (j - 11) <= 3:
                roleDescript = str(row[j])
                # print(something)
                mycursor.callproc('CreateRole', (roleDescript,))
                j += 1

        # company category ID
        if i == 0:
            j = 7
            while (j - 7) <= 3:
                companyCatID = str(row[j])
                # print(something)
                mycursor.callproc('CreateCompanyCategoryID', (companyCatID,))
                j += 1

        # status def
        if i == 0:
            statusDef = [row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31]]
            iterator = 22

            index = 0
            first = ''
            second = ''
            while iterator < 32:
                # print()
                if iterator % 2 == 0:
                    first = str(row[iterator])
                    # print(first)
                    iterator += 1
                else:
                    second = str(row[iterator])
                    # print(second)
                    mycursor.callproc('CreateStatusDefinition', (first, second))
                    iterator += 1

        # users
        users = row[32], row[33]

        mycursor.callproc('CreateUser', (str(row[32]),))
        if str(row[33]) != '':
            mycursor.callproc('UpdateUserDelete', (row[32], row[33]))

        # clients
        clients = row[0], row[1], row[2], row[3], row[4], row[5], row[6]
        mycursor.callproc('AddClient', clients)
        # print(row[5])

        mycursor.execute("select Client_ID from Client WHERE Email = %s ", (str(row[5]),))
        client_ID_out = mycursor.fetchall()  # returns a list with a tuple inside
        currClientID = 0
        for value in client_ID_out:  # iterate the list
            for num in value:  # iterate the tuple
                if num > 0:
                    currClientID = num
                    break
                elif num is None:
                    print('no jobs available')
                else:
                    print('something happened')
        # print(currClientID)
        contacts = ''
        # contacts
        if row[40] == '':
            contacts = (str(row[34]), str(row[35]), str(row[36]), str(row[37]), row[38], row[39], None)
        else:
            contacts = (str(row[34]), str(row[35]), str(row[36]), str(row[37]), row[38], row[39], row[40])
        # print(contacts)
        mycursor.callproc('CreateContact', contacts)

        # job
        jobs = (currClientID, row[16], row[17], row[18], row[19])
        mycursor.callproc('AddJob', jobs)

        # job cost
        jobCosts = (row[43], row[20], row[21])
        # print(jobCosts)
        mycursor.callproc('UpdateJobCost', jobCosts)

        # job sub details
        jobSubs = (row[41], row[42])
        mycursor.callproc('CreateJobSubDetails', jobSubs)

        # job status
        if row[45] != '':
            jobStatuses = row[41], row[46], row[45]
        else:
            jobStatuses = row[41], row[46], None
        # job_ident INT, IN stat_ID INT, IN date_created
        mycursor.callproc('UpdateJobStatus', jobStatuses)

        # job sales details
        jobSales = (row[41], row[43])
        mycursor.callproc('CreateJobSalesDetails', jobSales)

        i += 1
