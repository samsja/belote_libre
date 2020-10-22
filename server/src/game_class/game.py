from game_class.card import Color,Value,Card
from game_class.deck import Deck


class Atout:

    def __init__(self,color=0):
        self.color = Color(color)


class CardPlayed:

    def __init__(self,card,player):
        if not(isinstance(player,int)):
            raise TypeError(f"player should be an integer not {type(player)}")

        if not(isinstance(card,Card)):
            raise TypeError(f"card should be a Card not a {type(card)}")


        self.card = card
        self.player = player


class Game:

    nb_trick = 8
    nb_card_hand= 8
    nb_player = 4

    def __init__(self,rules,atout = Atout()):
        """Init a Game
        Keyword arguments:
        rules -- a list of AbstractRule
        """

        self.rules = rules
        self.atout = atout

        self.deck = Deck(shuffle=True)
        self.hands = [ self.deck[self.nb_card_hand*i:self.nb_card_hand*(i+1)] for i in range(self.nb_player)]
        self.tricks = [[]]

        self.next_player = 0
        self.over = False


    def validate_card(self,card,player):
        """Validate if a card could be play by the player
        Keyword arguments:
        card -- a Card instance
        player -- an int for the player index
        """

        if (not(isinstance(player,int)) or not(0<=player<self.nb_player)):
            raise TypeError(f"player should be an integer between 0 and {self.nb_player} not {type(player)}")

        if not(isinstance(card,Card)):
            raise TypeError(f"card should be a Card not {type(card)}")


        allowed = (card in self.hands[player]) and (self.next_player == player) and (not(self.over))

        if not(allowed):
            return allowed

        for rule in self.rules:
            if not(rule.is_play_allowed(self,card,player)):
                allowed=False
                break
        return allowed

    def _trick_winner(self,trick):
        """determine which player won the trick
        Keyword arguments:
        trick -- a 4 long list of player_card
        """
        return 0

    def play_a_card(self,card,player):
        """A player play a card.
        Keyword arguments:
        card -- a Card instance
        player -- an int for the player index
        """

        if (not(isinstance(player,int)) or not(0<=player<self.nb_player)):
            raise TypeError(f"player should be an integer between 0 and {self.nb_player} not {type(player)}")

        if not(isinstance(card,Card)):
            raise TypeError(f"card should be a Card not {type(card)}")

        if len(self.tricks)>=self.nb_trick:
            self.over = True

        if self.validate_card(card,player) :
            if len(self.tricks[-1]) == self.nb_player:
                self.tricks.append([])

            self.hands[player].remove(card)
            self.tricks[-1].append(CardPlayed(card,player))

            if len(self.tricks[-1]) == self.nb_player:
                self.next_player = self._trick_winner(self.tricks[-1])
            else:
                self.next_player = (self.next_player +1)%self.nb_player

            return True
        else:
            return False
