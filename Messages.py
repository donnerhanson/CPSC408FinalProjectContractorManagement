main_output_message = '1: Access Display Options\n' \
                      '2: Create new Record\n' \
                      '0: To exit...\n'
# '3: Update an individual student\n' \
# '4: Delete a student by Student ID\n' \
# '5: Search and Display students by Major, GPA, and Advisor\n' \


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
userRoleIDIn = 'enter user\'s role ID:\n'
# 5) Client - tbl 1
clientInName = 'Enter Client\'s name: \n'
# 6) Contacts - tbl 3
contactInName = 'Enter contact\'s name:\n '
# 7) Job - tbl 4
clientIDprompt = 'Enter Client\'s ID:\n'
estimatePrompt = 'Enter Estimate (Ex: 10000.00)\n:'
payoutPrompt = 'Enter Payout amount (Ex: 10000.00)\n:'
hoursPrompt = 'Enter amount of hours: \n'
jobCostIDPrompt = 'Enter jobCostID:\n'
# 8) Job Cost - tbl 5
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


def DisplayTableMessage(table_names):
    message = 'Press: '
    i = 1
    length = len(table_names)
    # print("length of table names ", len(table_names))
    for name in table_names:
        if i < length:
            message += str(i) + ' to display' + name + ' \n'
        else:
            message += str(i) + ' to display' + name
        i += 1
    message += '...\n'
    return message


first_name_prompt = 'First name: '
second_name_prompt = 'Last name: '
major_prompt = 'Major: '
GPA_prompt = 'GPA: '
faculty_advisor_prompt = 'Faculty Advisor: '
stud_id_prompt = 'Enter student ID: '

update_attribute_prompt = '1: To update major\n' \
                          '2: To update Faculty Advisor...\n'

search_attribute_prompt = '1: Search by major \n' \
                          '2: Search by GPA\n' \
                          '3: Search by Faculty Advisor...\n'

delete_confirmation = 'Are you sure you would like to delete:'

y_n = 'y/n: '
