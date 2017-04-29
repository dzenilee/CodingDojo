# Tues 4/4/17 Python Lecture Week 1 Session 2

# my_number = 42;
# print my_number

my_list = [41,23]
my_second_list = [
    42,
    24
]

# print my_list[1] + my_second_list[2] # list index out of range
# print

# try:
#     print my_list[1] + my_second_list[2]
# except IndexError:
#     print my_list[0] + my_second_list[1] #65


# try:
#     print my_list[1] + my_second_list[2]
# except (IndexError, TypeError):
#     print my_list[0] + my_second_list[1] #65

i,j = (1,2), [3,4] #the whole thing is still a tuple; we're UNPACKING it into into two different variables i and j (with j becoming just the value, in this case a list)
print i #(1,2)
print j #[3,4]
# i[1] = 42 #can't do item assignment to tuple
j[0] = 42
print i[1] + j[1] #can't do item assignment to tuple


i,j = (1,2), [3,4]
j[0] = 42
print i[1] + j[1] #2 + 4 = 6

j = 1, 2, 3
print j #(1,2,3)

j = (1,2), [3,4]
print j #((1,2), [3,4])
j[0] = 42 #can't do
print j

num = 1,2,3
print num #(1,2,3)

num1, num2, num3 = 1,3,5
print (num2) #3

a,b,c = 1,2,3
print a #1

i,j = 1, 2, 3
print j #error: too many values to unpack (not enough variables to hold them)

(i,j) = (1,2,3)
print j #error: too many values to unpack

(i,j),k = (1,2,3),6
print j #too many values to unpack

(i,j) = (1,2),3
print i #(1,2)
print j #3

our_list = ['Martin', 'Michael']
for val in enumerate(our_list):
    print val
# (0, 'Martin')
# (1, 'Michael')

for idx,value in enumerate(our_list):
    print value, idx
# Martin 0
# Michael 1

name = {"sw": "Sara Wong", "mp": "Martin Puryear"}
for key,value in name:
    print key,value #still going through the keys, but unpacking values "sw" and "mp" into variables key and value. These var names confuse you!
# s w
# m p

for bacon,chocolate in name:
    print bacon,chocolate
# s w
# m p

name = {"sw": "Sara Wong", "mp": "Martin Puryear"}
print name.items() #returns a list of (key-value tuples):
# [('sw', 'Sara Wong'), ('mp', 'Martin Puryear')]

for key, bacon in name.items():
    print key, bacon
# sw Sara Wong
# mp Martin Puryear

for chocolate in name.items(): #dictionary method
    print chocolate #returns each tuple in the list
# ('sw', 'Sara Wong')
# ('mp', 'Martin Puryear')

for candy in name.values():
    print candy
# Sara Wong
# Martin Puryear
