import deck
from vizu import stdout_vizu



v = stdout_vizu()

class SansAtout:

    def __init__(self,nb_player=4,card_deck=deck.BeloteDeck(),shuffle= True):

        if not(len(card_deck.set)%nb_player ==0):
            raise ValueError(f"the number of player : {nb_player}  should divide the total amount of card in the deck :{len(card_deck.set)}")


        self.card_deck = card_deck
        self.nb_player = nb_player

        self.next_player = 0

        self.pli = []
        self.all_pli = []

        if shuffle = True:
            self.card_deck.shuffle()

        self.nb_card_per_player = int(len(self.card_deck.set)/self.nb_player)

    def get_cards_player(self,player):
        n = int(len(self.card_deck.set)/self.nb_player)
        return self.card_deck.set[player*n:(player+1)*n]

    def get_opener_player(self):
        return 0

    def is_play_allow(self,card,player):
        if player != self.next_player :
            return False

        if not(card in self.get_cards_player(player)):
            return False

    def play_a_card(self,card,player):

        if not(self.is_play_allow(card,player)):
            return False


        self.pli.append([card,player])

        self.next_player = (self.next_player + 1)%self.nb_player

        if len(self.pli) == self.nb_player:

            self.all_pli.append(self.pli)
            self.pli = []
            self.next_player = self.get_opener_player()
            self.card_deck.shuffle()


        return True
