import numpy as np
from enum import Enum
from itertools import product


class Color(Enum):
    DIAMOND = 0
    SPADE = 1
    HEART = 2
    CLUB = 3


class Value(Enum):
    AS = 1
    TWO = 2
    THREE = 3
    FOR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    HEIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13




class Deck:

    def __init__(self):
        colors = np.arange(1,14)
        values = np.arange(0,4)

        self.set = np.array([ [colors,values ] for colors,values in product(colors,values)])


    def shuffle(self):
        np.random.shuffle(self.set)

    def roll(self):
        self.set = np.roll(self.set,np.random.randint(self.set.shape[0]))


class BeloteDeck(Deck):

    def __init__(self):
        super().__init__()

        self.set = self.set[(Value.SEVEN.value-1)*4 :Value.KING.value*4]
