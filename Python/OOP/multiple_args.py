"""
Multiple Arguments
What if you want to pass in a variable number of arguments, or want to
capture multiple arguments into a single parameter? Placing an asterisk
before the name of the parameter after the "normal'' parameters does just that.
The asterisk is called a 'splat' operator.
"""

def varargs(arg1, *args):
    # The method join() returns a string in which the string elements
    # of sequence have been joined by str separator.
    print "Got " + arg1 + " and " + ", ".join(args)

varargs("one") # Got one and
varargs("one", "two") # Got one and two
varargs("one", "two", "three") # Got one and two, three

# In this example, the first argument is assigned to the first method
# parameter as usual. However, the next parameter is prefixed with an
# asterisk(the "splat" operator we just introduced), which bundles the
# remaining arguments into a new tuple, which is then assigned to that parameter.

# If we tested the type of args inside our function using type(args) we would get:
def varargs(arg1, *args):
    print "args is of " + str(type(args))

varargs("one", "two", "three") # args is of <type 'tuple'>

# Note: the .join() method is called on a string that glues the values in the tuple
# together. For example, the tuple of arguments ('two', 'three') was joined as
# 'two, three' when we called ','.join(args).
