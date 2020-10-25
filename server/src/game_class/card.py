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
