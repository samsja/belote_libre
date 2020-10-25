from game_class.card import Color,Value,Card
from game_class.comparable import ComparabaleValue,ComparabaleCard

import copy

class Hand:

    def __init__(self,hand):

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

    def _order_little_hand(self,little_hand,atout_color):
        if len(little_hand) == 0:
            return little_hand


        atout = (little_hand[0].color == atout_color)
        comparable_little_hand = [ComparabaleCard(card,atout=atout) for card in little_hand]
        comparable_little_hand.sort(reverse=True)

        little_hand = [card.card for card in comparable_little_hand ]
        return little_hand

    def order(self,atout_color):

        hand_per_color = [[] for i in range(4)]

        for card in self:
            hand_per_color[card.color.value].append(card)

        for i,little_hand in enumerate(hand_per_color):
            hand_per_color[i] = self._order_little_hand(little_hand,atout_color)

        self.set = hand_per_color[Color.SPADE.value] + \
                   hand_per_color[Color.HEART.value] + \
                   hand_per_color[Color.CLUB.value]  + \
                   hand_per_color[Color.DIAMOND.value]
