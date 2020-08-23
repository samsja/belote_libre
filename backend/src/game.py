from deck import Deck,BeloteDdeck



class TurnbasedGame:

    def __init__(self,deck,nb_player):
        self.deck = deck
        self.n = nb_player

        self.list_card_played = []

    def play(self,index_card,index_player):
        if not(0 <= index_card < self.deck.set.shape[0]):
            raise ValueError(f"{index_card} should refer to an index in the set of the deck {self.deck.desc}")

        if not(-self.n < index_player < self.n):
            raise ValueError(f"{index_player} should refer to an index between {-self.n} and {self.n}")

        self.list_card_played.append(index_card)


class RulesException(Exception):
    def __init__(self, message):
        self.message = message


class PliBasedGame(TurnbasedGame):

    def __init__(self,deck,nb_player):
        super().__init__(deck,nb_player)
        self.list_last_players = []

    def play(self,index_card,index_player):

        if index_player in self.list_last_players:
            raise RulesException("this player has already played this turn")

        super().play(index_card,index_player)

        self.list_last_players.append(index_player)

        if len(self.list_last_players) == self.n:
             self.list_last_players = []

class Belote_game()
