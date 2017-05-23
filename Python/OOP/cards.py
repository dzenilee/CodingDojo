class BaseCard(object):
    def __init__(self, color, value):
        self.height = 5
        self.width = 3
        self.color = color
        self.value = value

    def card_info(self):
        print "Card Dimensions are " + str(self.height) + "inches x " + str(self.width) + "inches"
        return self

class UnoCard(BaseCard):
    # if I don't pass in anything, then my defaults are black and 'Draw 4'
    def __init__(self, color="black", value="Draw 4"):
        # setting values to BaseCard:
        # self here refers to the instance of the UnoCard that was created:
        super(UnoCard, self).__init__(color, value)
        self.face = "Uno"

    def card_info(self):
        print "**************************************"
        super(UnoCard, self).card_info()
        print "**************************************"
        print "Uno Card\n" + "Color: " + self.color + "\nvalue: " + self.value + "\nheight: " + str(self.height)
        return self

class PlayingCard(BaseCard):
    def __init__(self, suit="Joker", value=None):
        # you don't do self.color because we're not calling on it outside this function
        suit_color = None
        if (suit == "Hearts" or suit == "Diamonds"):
            suit_color = "red"
        elif (suit == "Spades" or suit == "Clubs"):
            suit_color = "black"
        # pass suit_color information into the BaseCard init function
        # that requires color to be passed in
        super(PlayingCard, self).__init__(suit_color, value)
        self.suit = suit

    def check_color(self):
        print "Playing Card is the " + str(self.value) + "of " + self.suit
        return self

card1 = PlayingCard("Hearts", 4)
print 'height:', card1.height
print  'width:', card1.width
print 'color:', card1.color

cardA = UnoCard("red", "two")
cardB = UnoCard("blue", "reverse")
# if I don't pass in anything, then my defaults are black and 'Draw 4'
cardC = UnoCard()
# Uno Card
# Color: black
# value: Draw 4

print cardA.card_info()
print cardB.card_info()
print cardC.card_info().card_info()
# Uno Card
# Color: black
# value: Draw 4
# Uno Card
# Color: black
# value: Draw 4
