"""
The objective of this assignment is to help you understand inheritance.
Remember that a class is more than just a collection of properties and methods.
If you want to create a new class with attributes and methods that are already
defined in another class, you can have this new class *inherit* from that other
class (called the parent) instead of copying and pasting code from the original
class. Child classes can access all the attributes and methods of a parent class
AND have new attributes and methods of its own, for child instances to call.

As we see with Wizard/Ninja/Samurai (that are each descended from Human), we can
have numerous unique child classes that inherit from the same parent class.
"""

# Create an Animal class and give it the below attributes and methods.
# Extend the Animal class to two child classes, Dog and Dragon.
class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 150
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print "Health:", self.health
        return self

# Create an instance of the Animal, have it walk() three times, run() twice,
# and finally displayHealth() to confirm that the health attribute has changed.
animal1 = Animal('animal_1')
print animal1.walk().walk().walk().run().run().displayHealth()

# Create a Dog class which inherits everything from Animal.
# Attributes: default health of 150
# Methods: pet(): increases health by 5
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name) # use super to call the Animal __init__ method
        self.health = 150
    def pet(self):
        self.health += 5
        return self

# Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().
dog1 = Dog('Beethoven')
print "{}'s health is {}".format(dog1.name, dog1.health)
print dog1.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name) # use super to call the Animal __init__ method
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self): # prints health by calling the parent method and prints "I am a Dragon"
        super(Dragon, self).displayHealth()
        print "I am a Dragon"
        return self

# Now try creating a new Animal and confirm that it cannot call the pet() and
# fly() methods and its displayHealth() is not saying 'this is a dragon!'
# Also confirm that your Dog class cannot fly().
dragon1 = Dragon('Doro')
# print dragon1.walk().walk().pet() # 'Dragon' object has no attribute 'pet'
print dragon1.walk().walk().run()
print dragon1.displayHealth()
