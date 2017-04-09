# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'}, #one item in list
#      {'first_name' : 'John', 'last_name' : 'Rosales'}, #one item in list
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'}, #one item in list
#      {'first_name' : 'KB', 'last_name' : 'Tonel'} #one item in list
# ]
#
def student_names(arr):
    for each in arr:
        full_name = each.values()
        print " ".join(full_name)

# student_names(students)
#output:
# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

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

for each in users['Students']:
    print each.values()
    # ['Michael', 'Jordan']
    # ['John', 'Rosales']
    # ['Mark', 'Guillen']
    # ['KB', 'Tonel']

def students_and_instructors(obj):
    for key in obj:
        print key #Students, Instructors
        name_count = 0
        for name in obj[key]:
            name_count += 1
            full_name = name.values()
            str_full_name = " ".join(full_name).upper()
            char_count = 0
            for char in str_full_name:
                char_count += 1
            print name_count, str_full_name, char_count-1  #capitalize names

students_and_instructors(users)
# output:
# Students
# 1 MICHAEL JORDAN 13
# 2 JOHN ROSALES 11
# 3 MARK GUILLEN 11
# 4 KB TONEL 7
# Instructors
# 1 MICHAEL CHOI 11
# 2 MARTIN PURYEAR 13
