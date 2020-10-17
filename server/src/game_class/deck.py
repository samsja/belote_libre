from game_class.card import Color,Value,Card
from itertools import product
import random

class Deck():

    # static set of cards
    set = [ Card(color,value) for color,value in product(range(4),range(Value.SEVEN.value,Value.AS.value+1))]


    def __init__(self,shuffle=True,seed=None):

        self.cards = list(range(32))
        if shuffle:
            self.shuffle(seed)

    def shuffle(self,seed=None):
        """Shuffle the deck.
        Keyword arguments:
        seed -- seed value for random, default int, awaited int
        """

        if not(seed) == None:
            random.seed(seed)

        random.shuffle(self.cards)

    def __getitem__(self, key):
        """return the key-th cards"""

        if isinstance(key, slice):
          start, stop, step = key.indices(len(self.cards))
          return [self[i] for i in range(start, stop, step)]
        elif isinstance(key, int):
            return self.set[self.cards[key]]
        else:
            raise TypeError(f"key should be int or slice not {type(key)}")
