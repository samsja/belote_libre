from game_class.card import Color,Value,Card
from game_class.comparable import ComparabaleValue

import copy

class Hand:

    def __init__(self,hand=[]):

        for card in hand:
            if not(isinstance(card,Card)):
                raise TypeError(f"card should be a Card not {type(card)}")

        self.set = copy.deepcopy(hand)

    def __getitem__(self,key):
        return self.set[key]

    def __len__(self):
        return len(self.set)

    def remove(self,card):
        return self.set.remove(card)

    def _order_little_hand(self,little_hand):
        pass

    def order(self,atout_color):

        hand_per_color = [[] for i in range(4)]

        for card in self:
            hand_per_color[card.color.value].append(card)

        for little_hand in hand_per_color:
            self._order_little_hand(little_hand)

        self.set = hand_per_color[Color.SPADE.value] + \
                   hand_per_color[Color.HEART.value] + \
                   hand_per_color[Color.CLUB.value]  + \
                   hand_per_color[Color.DIAMOND.value]
