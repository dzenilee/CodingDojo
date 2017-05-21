class Vehicle(object):
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0

    def drive(self, miles):
        self.miles += miles
        return self

    def reverse(self, miles):
        self.mile -= miles
        return self

# Implicit inheritance
# Now we want to create new (sub)classes that are able to use all of the function
# and properties in the Vehicle class but also have some of their own additional
# functions and properties.

# Classes Car, Bike, and Airplane all inherit the blueprint of class Vehicle,
# but in addition, they add their own blueprint. Now to create our new classes
# in a file called new_classes.py:

class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"

class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self

class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self

# Create some instances
v = Vehicle(4, 8, "dodge", "minivan")
print v.make

b = Bike(2, 1, "Schwinn", "Paramount")
print b.vehicle_type()

c = Car(8, 5, "Toyota", "Matrix")
print c.wheels # 8
c.set_wheels()
print c.wheels # 4

a = Airplane(22, 853, "Airbus", "A380")
a.fly(580)
print a.mileage # 580

# When we defined each of our classes, we typed Bike(Vehicle), Car(Vehicle),
# and Airplane(Vehicle). You could read each of these like "Make a class
# Bike/Car/Airplane that inherits from Vehicle".
# This is what is known as the implicit inheritance which allows us to
# use inherited attributes and methods of the Vehicle(parent) class in
# our new subclasses.
