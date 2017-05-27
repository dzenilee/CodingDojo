"""
You're creating a program for a call center. Every time a call comes in
you need a way to track that call. One of your program's requirements is to
store calls in a queue while callers wait to speak with a call center employee.

You will create two classes. One class should be Call, the other CallCenter.

Call Class
Create your call class with an init method. Each instance of Call() should have:

Attributes:
* unique id
* caller name
* caller phone number
* time of call
* reason for call

Methods:
* display: that prints all Call attributes.
"""

class Call(object):
    def __init__(self, id, name, number, time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

    def display(self):
        print "The caller's id is {}, their name is {}, their phone number is {}, they called at {}, their reason for calling is {}".format(self.id, self.name, self.number, self.time, self.reason)
        return self

# Create an instance of the Call class
call1 = Call("1", "George", "488-440-1123", "3:30 PM", "to say hello")
call2 = Call("2", "Sarah", "112-332-1919", "1:30 AM", "I'm bored")
# print call1.display()

"""
CallCenter Class
Create you call center class with an init method. Each instance of CallCenter() should have the following attributes:
Attributes:
* calls: should be a list of call objects
* queue size: should be the length of the call list

Methods:
* add: adds a new to the end of the call list
* remove: removes the call from the beginning of the list (index 0).
* info: prints the name and phone number for each call in the queue as well as the length of the queue.
"""

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    # add a new call to the end of call list
    def add(self, *new_calls):
        for new_call in new_calls:
            self.calls.append(new_call)
            self.queue_size += 1
        return self

    # remove the call from the beginning of the list (index 0)
    def remove(self):
        self.calls.pop(0)
        return self

    # print the name and number for each call in the queue + the length of queue
    def info(self):
        for call in self.calls:
            print "Name: {}, phone number: {}".format(call.name, call.number)
        print "Length of queue: {}".format(self.queue_size)

# Create an instance of the CallCenter class
callcenter1 = CallCenter()
callcenter1.add(call1, call2).remove().info()
