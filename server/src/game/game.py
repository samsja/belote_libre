from card import Color,Value,Card
from deck import Deck



class CardPlayed:

    def __init__(self,card,player):

        if not(isinstance(player,int)):
            raise TypeError(f"player should be an integer not {type(player)}")

        if not(isinstance(card,Card)):
            raise TypeError(f"card should be a Card {type(card)}")

        self.card = card
        self.player = player


class Game:

    nb_trick = 8
    nb_card_hand= 8
    nb_player = 4

    def __init__(self):

        self.deck = Deck(shuffle=True)
        self.hands = [ self.deck[i:self.nb_card_hand*(i+1)] for i in range(self.nb_player)]
        self.tricks = [[]]


    def _validate_card(self,card,player):
        return (card in self.hands[player])

    def play_a_card(self,card,player):
        """A player play a card.
        Keyword arguments:
        card -- a tuple (color,value) representatin the card
        player -- an int for the player index
        """

        if (not(isinstance(player,int)) or not(0<=player<self.nb_player)):
            raise TypeError(f"player should be an integer between 0 and {self.nb_player} not {type(player)}")

        if not(isinstance(card,Card)):
            raise TypeError(f"card should be a Card {type(card)}")

        if self._validate_card(card,player):
            self.hands[player].remove(card)
            self.tricks[-1].append(CardPlayed(card,player))

            if len(self.tricks[-1]) == self.nb_player:
                self.trick.append([])

            return True
        else:
            return False

g = Game()
