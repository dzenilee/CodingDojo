#Imagine that your program input will always be an array. For each item in the array, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the array contains. If it contains only one type, print that type, otherwise, print 'mixed'.

def check_type(lst):
    if all(isinstance(each, str) for each in lst):
        array_type = "string type"
        print print_type() + array_type
        print_str(lst)
    elif all(isinstance(each, int) for each in lst):
        array_type = "integer type"
        print print_type() + array_type
        print_sum(lst)
    else:
        if any(isinstance(each, str) for each in lst):
            array_type = "mixed type"
            print print_type() + array_type
            print_str(lst)
            print_sum(lst)
        else:
            array_type = "number type"
            print print_type() + array_type
            print_sum(lst)

def print_type():
    return "The array you entered is of "

def print_sum(lst):
    sum = 0
    for each in lst:
        if isinstance(each, int) or isinstance(each, float):
            sum += each
    print "Sum:", sum

def print_str(lst):
    string = ""
    for each in lst:
        if isinstance(each, str):
            string = string + each + " "
    print "String:", string

m = ['hi', 'there']
check_type(m)

l = ['magical unicorns',19,'hello',98.98,'world']
check_type(l)
# "The array you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"

k = [2,3,1,7,4,12]
check_type(k)
# "The array you entered is of integer type"
# "Sum: 29"
