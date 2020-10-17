import numpy as np

class StupidPlayer:

    def select_an_action(self,cards):
        return cards[0]

class RandomPlayer:

    def select_an_action(self,cards):
        return cards[np.random.randint(len(cards))]
