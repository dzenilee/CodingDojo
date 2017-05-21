"""
Sometimes in your OOP code, you will want to create updated versions of
methods that are defined in the parent class, because in addition to your
custom code you want specifically to call the parent implementation of that
method as well (or instead). In these cases, you would reference that parent
object with the keyword 'super'. Specifically you reference that parent's
method by calling 'super(ChildClassName, self).parent_method()'

One thing we may want to do is call the Parent class's __init__ method,
but also have our Child class change attributes defined by its Parent class.
Say that we wanted each of our sub-classes (Wizard, Ninja, Samurai) to still
inherit the attributes of the parent Human class but have more developed
attributes than the average Human. We could do that like this:
"""

from human import Human
class Wizard(Human):
    def __init__(self):
        super(Wizard, self).__init__() # use super to call the Human __init__ method
        self.intelligence = 10 # every wizard starts off with 10 intelligence
    def heal(self):
        self.health += 10

class Ninja(Human):
    def __init__(self):
        super(Ninja, self).__init__() # use super to call the Human __init__ method
        self.stealth = 10 # every Ninja starts off with 10 stealth
    def steal(self):
        self.stealth += 5

class Samurai(Human):
    def __init__(self):
        super(Samurai, self).__init__() # use super to call the Human __init__ method
        self.strength = 10 # every Samurai starts off with 10 strength
    def sacrifice(self):
        self.health -= 5

"""
If we create instances of each, we'll see that they have the same attributes as
the typical Human (the parent class), but they also have beefed up attributes
depending on which subclass we instantiated. Notice how we call the __init__
method of the super(parent). Other methods are called the same way with the
exception of passing in variables.
""" 
