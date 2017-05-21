"""
Now, let's build a store to contain our products by making
a store class and putting out products into an array.

Store class:
Attributes:
# products: an array of products objects
# location: store address
# owner: store owner's name

Methods:
# add_product: add a product to the store's product list
# remove_product: should remove a product according to the product name
# inventory: print relevant information about each product in the store

You should be able to test your classes by instantiating new objects of
each class and using the outlined methods to demonstrate that they work.
"""

class Store(object):
    # the __init__ method is called every time a new object is created.
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner

    # methods 
