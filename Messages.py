#display
#parameterized search
#update
#create
#delete
#export
# MAIN
main_output_message = '1: Access Display Options\n' \
                      '2: Parameterized Search\n' \
                      '3: Update an existing record\n' \
                      '4: Create a new record\n' \
                      '5: Delete a record\n' \
                      '0: To exit...\n'

# UPDATE TABLE
update_table_prompt = '1: To update Client Information\n' \
                            '2: To update Job/Job Cost...\n' \
                            '3: To update Contact Information\n' \
                            '4: To update User (Employee Information)...\n'

update_table_prompt = '1: To update Client Information\n' \
                      '2: To update Job/Job Cost...\n' \
                      '3: To update Contact Information...\n' \
                      '4: To update User (Employee Information)\n'


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

update_job_search_options = 'If searched contact does not exist this current\n' \
                                'process will exit without changes to the system...\n' \
                                '1: Find Job by ID\n' \
                                '2: Find Job by Client ID\n' \
                                '3: Find Job by Date\n' \
                                '0: Exit Update Process...\n'

update_job_attributes = '1: Update Estimate\n' \
                                '2: Update Payout\n' \
                                '3: Update Hours\n' \
                                '4: Update Status\n' \
                                '5: Update Additional Misc. Costs\n' \
                                '6: Update Material Costs\n' \
                                '0: Exit Update...\n'


# a) Misc
addressInMessage = 'Enter Street Address\n'
cityInMessage = 'Enter City:\n'
stateInMessage = 'Enter State (Ex: \'CA\'): \n'
zipInMessage = 'Enter Zip (Ex: \'92868\'): \n'
phoneInMessage = 'Enter phone number (Ex: \'555-555-5555\'): \n'
emailInMessage = 'Enter email: \n'

# 1) Roles - tbl 9
roleInMessage = 'Enter a Role Description:\n'
# 2) CompanyCategoryTableLookup - tbl 2
companyCategoryTableLookupIn = 'Enter a company category type: (Ex: Plumbing, Multiple Purpose, Etc)\n'
# 3) StatusDefinition - tbl 10
statusDefinitionInNameMessage = 'Enter a new status name:\n'
statusDefinitionInDescriptionMessage = 'Enter a new status name:\n'
# 4) Users - tbl 11
userRoleIDIn = 'Enter user\'s role ID:\n'
userInName = 'Enter User\'s name: \n'
# 5) Client - tbl 1
clientInName = 'Enter Client\'s name: \n'
# 6) Contacts - tbl 3
contactIDprompt = 'Enter Contact\'s ID:\n'
contactInName = 'Enter Contact\'s Name:\n '
contactInEmail = 'Enter Contact\'s Email:\n '
contactInURL = 'Enter Contact\'s URL:\n '
# 7) Job - tbl 4
clientIDprompt = 'Enter Client\'s ID:\n'
estimatePrompt = 'Enter Estimate (Ex: 10000.00)\n:'
payoutPrompt = 'Enter Payout amount (Ex: 10000.00)\n:'
hoursPrompt = 'Enter amount of hours: \n'
jobCostIDPrompt = 'Enter jobCostID:\n'
# 8) Job Cost - tbl 5
additionsInPrompt = 'Enter the total of miscellaneous Additions: \n'
materialsInPrompt = 'Enter the amount of additional Materials: \n'
# 9) JobSubDetails - tbl 8
jobSubJobIDIn = 'Enter job ID: \n'
jobSubContactIDIn = 'Enter Contact ID: \n'
# 10) JobStatus - tbl 7
jobIDPrompt = 'Enter Job_ID\n:'
statusIDprompt = 'Enter Status_ID\n:'
# 11) JobSalesDetails - tbl 6
##jobIDPrompt
userIDPrompt = 'Enter User ID\n'

# USERINPUT CHOICES
# display
display_all = 'Display all?'

dateInPrompt = 'Input date ex: 10/30/2009'

def DisplayTableMessage(table_names):
    message = 'Input: \n'
    i = 1
    length = len(table_names)
    # print("length of table names ", len(table_names))
    for name in table_names:
        if i < length:
            message += str(i) + ' to display ' + name + ' \n'
        else:
            message += str(i) + ' to display ' + name
        i += 1
    message += '...\n'
    return message


parameterLookupMenu = 'Search for:\n1. Jobs\n2. Clients \n3. Contacts\n4. Users\n'
parameterJobLookup = 'Search for:\n 1. Employees attached to Job\n2. Subcontractors attached to Job\n3. Costs attached to Job\n'
parameterClientLookup = 'Search for:\n1. Jobs attached to Client\n2. Costs from Client\n'
parameterContactLookup = 'Search for:\n1. Jobs attached to Contact\n'
parameterUserLookup = 'Search for:\n1. Jobs attached to User\n'





first_name_prompt = 'First name: '




search_attribute_prompt = '1: Search by major \n' \
                          '2: Search by GPA\n' \
                          '3: Search by Faculty Advisor...\n'

delete_confirmation = 'Are you sure you would like to delete:'

y_n = 'y/n: '
