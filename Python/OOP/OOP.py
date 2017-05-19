class User(object):
    name = "Anna"

# when we call methods, no need to pass in any arguments (known as implicit passage of self)
anna = User()
print "anna's name: ", anna.name # Anna

# we can change the state of the single object by making modifications only to self
User.name = "Bob"
print "anna's name after change:", anna.name # Bob

bob = User()
print "bob's name:", bob.name # Bob

print User().name # Bob

################################################
class User(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, name, email):
        # set some instance variables, just like any variable, we can call these anything
        self.name = name
        self.email = email
        self.logged = False
    # this is a method we created to help a user login
    def login(self):
        self.logged = True
        print self.name + "is logged in."
        return self 

user1 = User("Anna Propas", "anna@anna.com")
print user1.name
print user1.logged
print user1.email

################################################
