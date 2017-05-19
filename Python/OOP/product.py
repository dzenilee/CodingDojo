"""
The owner of a store wants a program to track products.
Create a product class to fill the following requirements.

Product Class:
Attributes:
# Price
# Item Name
# Weight
# Brand
# Cost
# Status: default "for sale"

Methods:
# Sell: changes status to "sold"

# Add tax: takes tax as a decimal amount as a parameter and
# returns the price of the item including sales tax

# Return: takes reason for return as a parameter and changes status accordingly.
# If the item is being returned because it is defective change status to defective
# and change price to 0. If it is being returned in the box,
# like new mark it as for sale. If the box has been opened set status to used
# and apply a 20% discount.

# Display Info: show all product details.

# Every method that doesn't have to return something should
# return self so methods can be chained.
"""

class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'

    def Sell(self):
        self.status = "sold"
        return self

    def AddTax(self, tax):
        self.price = self.tax * self.price
        return self

    def Return(self, reason):
        self.status = reason
        if "defective" in self.status:
            self.status = "defective"
            self.price = 0
        elif "in the box" in self.status:
            self.status = "for sale"
        elif "opened" in self.status:
            self.status = "used"
            self.price = .8 * self.price
        return self

    def DisplayInfo(self):
        print "Price:", self.price
        print "Item name:", self.item_name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        return self

#create instances of the class Product
product1 = Product('$400', 'vacuum cleaner', '30lbs', 'Hoover')

print product1.DisplayInfo()
