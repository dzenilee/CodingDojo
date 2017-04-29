# Tues 4/4/17 Python Lecture Week 1 Session 2

# DICTIONARIES ## DICTIONARIES #

student = {
    "first_name": "Randy",
    "last_name": "Ventura",
    "age": [12, 15, 25, 40, 67]
}

student["first_name"] = "Michelle"
print student["first_name"]

There is no indexing of dictionary
for item in student:
    print item # prints keys 
# output:
# first_name
# last_name
# age

# How can we get value for each key, then?
for item in student:
    print student[item]
# output:
# Michelle
# Ventura
# 67

print student['age'][2] #25

for item in student:
    print item, student[item]

# FUNCTIONS ## FUNCTIONS #
def ourFunction(num):
    print 'hello\n' * num

# ourFunction(8)

for number in range(10):
    ourFunction(2)
