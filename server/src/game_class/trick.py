from game_class.card import Color,Value,Card,CardPlayed
from game_class.comparable import ComparabaleValue


class Trick:

    def __init__(self,trick=[]):

        for card_played in trick:
            if not(isinstance(card_played,CardPlayed)):
                raise TypeError(f"card_played should be a CardPlayed not {type(card_played)}")

        self.set = trick


    def __getitem__(self,key):
        return self.set[key]

    def __len__(self):
        return len(self.set)

    def append(self,card_played):
        if not(isinstance(card_played,CardPlayed)):
            raise TypeError(f"card_played should be a CardPlayed not {type(card_played)}")

        self.set.append(card_played)

    def _select_max_in_colors(self,list_cards_played,atout):
        values = []
        for card_played in list_cards_played:
            values.append(ComparabaleValue(card_played.card.value,atout=atout))

        winner = values.index(max(values)) ## arggh no arg max is python :( not very effective thow
        return list_cards_played[winner].player

    def winner(self,atout_color):
        if len(self.set) == 0:
            raise ValueError(f" the trick is empty {self.set}")


        main_color = self.set[0].card.color

        main_color_cards_played = []
        atout_color_cards_played= []

        for card_played in self.set:
            if card_played.card.color == main_color:
                main_color_cards_played.append(card_played)
            if card_played.card.color == atout_color:
                atout_color_cards_played.append(card_played)

        if len(atout_color_cards_played) > 0:
            return self._select_max_in_colors(atout_color_cards_played,atout=True)

        elif len(main_color_cards_played) > 0:
            return self._select_max_in_colors(main_color_cards_played,atout=False)

        else:
            raise ValueError("we are missing some color here")
