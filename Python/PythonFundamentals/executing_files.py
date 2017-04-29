print "Hello World"
print str(23) #23
print int('1') + 2 #3
#print '1' + 2 # error

x = "Hello Python"
print x
y = 42
print y

# COMMENTING
"""
Triple quotations allow us to comment multiple lines as long as
the triple quoted comment is not the first thing in your file.
You can use double or single quotes!
"""

# DEFINE A FUNCTION that says hello to the name provided
def say_hello(name):
    if name:
        print 'Hello, ' + name + ' from inside the funciton'
    else:
        print 'No name'

say_hello("Jenny")

print 'Outside of the function'

name = "Zen"
num = 3
print "My name is" + name #My name isZen
print "My name is", name #My name is Zen
# print "My name is" + num #Will throw an error
print "My name is", num #My name is 3

# STRING INTERPOLATION
# Use curly brackets - {} - and the string .format() method to inject variables into your string.
# There should be a corresponding number of curly brackets and arguments passed to the .format() function

first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

# soon to be deprecated:
hw = "hello %s" % "world"
print hw #hello world

# BUILT-IN STRING METHODS: see more - https://docs.python.org/2.6/library/string.html
from string import *
x = "hello world"
# Return a copy of word with only its first character capitalized.
# I think this one's deprecated
print x.capitalize() #Hello world

# LISTS
ninjas = ['Rozen', 'KB', 'Oliver']
ninjas.append('BOYN')
print ninjas #['Rozen', 'KB', 'Oliver', 'BOYN']

my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

#In Python, the elements of a list do not have to be of the same data type. A list can be a mixture of any Python data types, including, tuples, strings, numeric, and even a list itself (a list within a list). An example:
fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']

fruits_and_vegetables = fruits + vegetables
print fruits_and_vegetables #['apple', 'banana', 'orange', 'strawberry', 'lettuce', 'cucumber', 'carrots']
salad = 3 * vegetables
print salad #['lettuce', 'cucumber', 'carrots', 'lettuce', 'cucumber', 'carrots', 'lettuce', 'cucumber', 'carrots']

# MANIPULATING LISTS
x = [1,2,3,4]
x.append(99)
print x #[1,2,3,4,5,99]

#It's important to know that Python uses [ ] characters to return a copy of the list, constrained to the specified indices. This can be thought of as behaving like the slice function in JavaScript. The starting index and ending index should be separated by the ":" character.

x = [99, 4, 2, 5, 03]
#x[this_index:upto_and_not_including]
print x[:] #[99, 4, 2, 5, 3]
print x[1:] #[4, 2, 5, 3]
print x[:4] #[99, 4, 2, 5]
print x[2:4] #[2,5]

# LIST BUILT-IN FUNCTIONS
my_list = [1, 'Zen', 'hi']
print len(my_list) #3

# CONDITIONAL EXPRESSIONS
age = 15
if age >= 18:
    print 'Legal age'
elif age == 17:
    print 'You are seventeen'
else:
    print 'You are so young!'

# LOOPS
for count in range(0,5):
    print "looping - ", count

# LOOPING THROUGH A LIST
my_list = [4, 'dog', 99, ['list', 'inside', 'another'], 'hello world!']
for element in my_list:
    print element

# WHILE LOOPS
count = 0
while count < 5:
    print 'looping -', count
    count += 1


# BREAK: The most common use for the break is when some external condition is triggered, requiring a hasty exit from a loop. The break statement can be used in both while and for loop. When loops are nested, a break will only exit from the innermost loop.

for val in 'string':
    if val == 'i':
        break
    print val # s t r

# CONTINUE: The continue statement RETURNS the control TO THE BEGINNING OF THE LOOP. The continue statement rejects -- or skips -- all the remaining statements in the CURRENT ITERATION OF THE LOOP, and continues normal execution at the top of the loop. The continue statement is very useful when you want to skip one or more loop iterations, BUT KEEP LOOPING TO THE END.

for val in 'string':
    if val == 'i':
        continue
    print val # s t r n g

# PASS: when a statement is required syntactically but you do not want any command or code to execute.
class EmptyClass:
    pass

my_string = "this is my string"
for val in my_string:
    pass

# ELSE
x = 3
y = x
while y > 0:
    print y
    y = y - 1
else:
    print 'Final else statement'
# Note that the above else code section is only executed if the while loop runs normally and its conditional is false (whether we never entered the while loop, or we did but eventually the conditional changed from true to false).

# If instead our while loop is exited prematurely because of a breka or return statement, the else code section will never be executed.
x = 3
y = 3
while y > 0:
    print y
    y -= 1
    if y == 0:
        break
else:
    print "Final else statement"

x = None
if not x:
    print 'x contains nothing!'
