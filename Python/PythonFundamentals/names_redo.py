# PART 1
# Given:
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# Create a program that outputs:
# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

# for each in students: # each is an object
#     # print each # prints each object in list
#     print each['first_name'], each['last_name'] # prints the value of each object's 'first_name' and 'last_name'

# PART 2
# Now, given the following dictionary:

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# Create a program that prints the following format (including number of characters in each combined name):
# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13

def name_and_length(obj):
    for item in obj:
        print item
        # Students
        # Instructors
        # print obj[item]
        # [{'first_name': 'Michael', 'last_name': 'Jordan'}, {'first_name': 'John', 'last_name': 'Rosales'}, {'first_name': 'Mark', 'last_name': 'Guillen'}, {'first_name': 'KB', 'last_name': 'Tonel'}]
        # [{'first_name': 'Michael', 'last_name': 'Choi'}, {'first_name': 'Martin', 'last_name': 'Puryear'}]
        counter = 0;
        for person_obj in obj[item]:
            counter += 1
            fn = len(person_obj['first_name'])
            ln = len(person_obj['last_name'])
            print counter, '-', person_obj['first_name'].upper(), person_obj['last_name'].upper(), '-', fn+ln
        # for person in obj[item]:
        #     print person['first_name'], person['last_name']   # need to access the values of the keys

name_and_length(users)
