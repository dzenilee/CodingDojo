# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
def odd_even():
    for each in range(1,20):
        if each % 2 == 0:
            print "Number is {}. This is an even number.".format(each)
        else:
            print "Number is {}. This is an odd number.".format(each)

odd_even()

# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
def multiply(lst, num):
    new_lst = []
    for ea in lst:
        new_lst.append(ea * num)
    return new_lst

a = [2, 4, 10, 16]
multiply([2, 4, 10, 16], 5) #[10, 20, 50, 80]

# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the number of 1's as the number in the original list.

def layered_multiples(arr):
    new_array = []
    for each in arr: #each = 6, 12, 15 
        inner_array = []
        for i in range(0, each):
            inner_array.append(1)
        new_array.append(inner_array)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
