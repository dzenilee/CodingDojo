# HINT: To do this exercise, you will probably have to use 'return self'.
# If the method returns itself (an instance of itself), we can chain methods.

"""
Part 1
Create a Python class called MathDojo that has the methods add and subtract.
Have these 2 functions take at least 1 parameter.
Then create a new instance called md. It should be able to do the following task:

MathDojo().add(2).add(2, 5).subtract(3, 2).result

which should perform 0+2+(2+5)-(3+2) and return 4.
"""

class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for arg in args:
            self.result += arg
        return self
    def subtract(self, *args):
        for arg in args:
            self.result -= arg
        return self

# print MathDojo().add(2).add(2, 5).subtract(3,2).result

"""
PART II
Modify MathDojo to take at least one integer(s) and/or list(s) as a
parameter with any number of values passed into the list.
It should now be able to perform the following tasks:

MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result

should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.
"""

class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for arg in args:
            if type(arg) is list:
                for item in arg:
                    self.result += item
            elif type(arg) is int:
                self.result += arg
        return self
    def subtract(self, *args):
        for arg in args:
            if type(arg) is list:
                for item in arg:
                    self.result -= item
            elif type(arg) is int:
                self.result -= arg
        return self

print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result # 28.15

"""
PART III
Make any needed changes in MathDojo in order to support tuples of values
in addition to lists and singletons.
"""

class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for arg in args:
            if type(arg) is list or type(arg) is tuple:
                for item in arg:
                    self.result += item
            elif type(arg) is int:
                self.result += arg
        return self
    def subtract(self, *args):
        for arg in args:
            if type(arg) is list or type(arg) is tuple:
                for item in arg:
                    self.result -= item
            elif type(arg) is int:
                self.result -= arg
        return self

print MathDojo().add((1,6,7,8,9)).subtract(2, [3, 4, 2, -1, 3, 2]).add([2,3,4,5], 2).result # 32
