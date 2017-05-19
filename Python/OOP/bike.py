# Create a new class called Bike with the following properties/attributes:
# price, max_speed, miles

# Create 3 instances of the Bike class.

# Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.

# Add the following functions to this class:

# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...

class Bike(object):
    # the __init__ method is called every time a new object is created.
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    # have this method display the bike's price, maximum speed, and the total miles.
    def displayInfo(self):
        print "This bike is priced at ${}, runs at a maximum speed of {}mph, and runs a total of {} miles.".format(self.price, self.max_speed, self.miles)
        return self

    def ride(self):
        self.miles += 10
        print "Riding:", self.miles
        return self

    def reverse(self):
        self.miles -= 5
        print "Reversing:", self.miles
        return self

# create instances of the class Bike
bike1 = Bike(300, 80)
bike2 = Bike(400, 100)
bike3 = Bike(1000, 130)

# print type(bike1)
print bike1.ride().ride().ride().reverse().displayInfo()
print bike2.ride().ride().reverse().reverse().displayInfo()
print bike3.reverse().reverse().reverse().displayInfo() 
