from card import BeloteCard
from itertools import product
import numpy as np


class Deck:

    def __init__(self,deck_list,desc):
        if isinstance(deck_list,np.ndarray):
            self.set = deck_list
        else:
            self.set = np.array(deck_list)

        self.desc = desc

    def __str__(self):
        str_return = "=======" + self.desc + "========="
        for card in self.set:
                str_return=str_return + "\n" +  card.desc
        return str_return

    def shuffle(self):
        np.random.shuffle(self.set)

    def roll(self):
        self.set = np.roll(self.set,np.random.randint(self.set.shape[0]))


class BeloteDeck(Deck):

    def __init__(self,shuffle=True):
        deck = []
        for color,value in product(BeloteCard.colors,BeloteCard.values):
            deck.append(BeloteCard(color,value))

        super().__init__(deck,"Jeu de Belote")

        if shuffle:
            self.shuffle()
