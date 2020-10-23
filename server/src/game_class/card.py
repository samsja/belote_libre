from enum import IntEnum

class Color(IntEnum):
    DIAMOND = 0
    SPADE = 1
    HEART = 2
    CLUB = 3


class Value(IntEnum):
    SEVEN = 0
    HEIGHT = 1
    NINE = 2
    TEN = 3
    JACK = 4
    QUEEN = 5
    KING = 6
    AS = 7


class Card:

    def __init__(self,color,value):

        self.color = Color(color)
        self.value = Value(value)


    def __str__(self):
        return f"{Color(self.color).name},{Value(self.value).name}"



class CardPlayed:

    def __init__(self,card,player):
        if not(isinstance(player,int)):
            raise TypeError(f"player should be an integer not {type(player)}")

        if not(isinstance(card,Card)):
            raise TypeError(f"card should be a Card not a {type(card)}")


        self.card = card
        self.player = player


normal_order = [ Value.SEVEN,
                Value.HEIGHT,
                Value.NINE,
                Value.JACK,
                Value.QUEEN,
                Value.KING,
                Value.TEN,
                Value.AS,
    ]

atout_order = [ Value.SEVEN,
                Value.HEIGHT,
                Value.QUEEN,
                Value.KING,
                Value.TEN,
                Value.AS,
                Value.NINE,
                Value.JACK,
    ]

def is_better(value1,value2,atout=False):
    """Return True if value1 is better than Value2
    Keyword arguments:
    value1 -- a Value enum
    value2 -- a Value enum
    atout -- Boolean , default : False , tell if we need to take atout order
    """
    if atout:
        order = atout_order
    else:
        order = normal_order

    if value1 == value2:
        return False
    else:
        i1 = order.index(value1.value)
        i2 = order.index(value2.value)

        return i1>i2


class ComparabaleValue:

    def __init__(self,value,atout=False):
        self.value = value

        if atout:
            self.order = atout_order
        else:
            self.order = normal_order

        self.i1 = self.order.index(self.value)

    def __gt__(self, other):
        i2 = self.order.index(other)
        return self.i1>i2

    def __ge__(self, other):
        i2 = self.order.index(other)
        return self.i1>=i2

    def __lt__(self, other):
        i2 = self.order.index(other)
        return self.i1<i2

    def __le__(self, other):
        i2 = self.order.index(other)
        return self.i1<=i2

    def __eq__(self, other):
        i2 = self.order.index(other)
        return self.i1==i2

    def __ne__(self, other):
        return not(self.__eq__(other))


def trick_winner(trick):
    pass
