class Card(object):
    def __init__(self, suit = "Hearts", val = "Joker"):
        self.suit = suit
        self.value = val
        # self.color = "red"
    def check_color(self):

        if self.suit == "Hearts" or self.suit == "Diamonds":
            self.color = "red"
        elif self.suit == "Spades" or self.suit == "Clubs":
            self.color = "black"
        else:
            self.color = "None"

        print self.color, self.suit, self.value

card1 = Card("Clubs", 3)
card2 = Card("Hearts", 3)
card3 = Card("Diamonds", 3)
card4 = Card("Spades", 3)
card5 = Card("Clubs", 13)
card6 = Card("Hearts", 13)
card7 = Card("Diamonds", 13)
card8 = Card() # __init__() takes exactly 3 arguments (1 given) i.e., self given
card9 = Card(10)

# print card1.suit
# print card2.suit
# print card3.suit
# print card4.suit
# print card8.value
# print card9.value, card9.suit
card8.check_color()
card7.check_color()
card6.check_color()
card5.check_color()
