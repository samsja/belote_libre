import deck as deck


class Bataille:

    def __init__(self,nb_player=4,card_deck=deck.Deck):

        self.card_deck = card_deck
        self.nb_player = nb_player


        self.next_player = 0

        self.pli = []
        self.all_pli = []

    def play_a_card(self,card,player):

        if player != self.next_player :
            return False

        self.pli.append(card)

        self.next_player = self.next_player + 1

        if self.next_player == self.nb_player:

            self.all_pli.append(pli)
            self.next_player = 0

        return True
