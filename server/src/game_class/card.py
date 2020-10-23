from enum import IntEnum

class Color(IntEnum):
    DIAMOND = 0
    SPADE = 1
    HEART = 2
    CLUB = 3


class Value(IntEnum):
    SEVEN = 0
    HEIGHT = 1
    NINE = 2
    TEN = 3
    JACK = 4
    QUEEN = 5
    KING = 6
    AS = 7


class Card:

    def __init__(self,color,value):

        self.color = Color(color)
        self.value = Value(value)


    def __str__(self):
        return f"{Color(self.color).name},{Value(self.value).name}"



class CardPlayed:

    def __init__(self,card,player):
        if not(isinstance(player,int)):
            raise TypeError(f"player should be an integer not {type(player)}")

        if not(isinstance(card,Card)):
            raise TypeError(f"card should be a Card not a {type(card)}")


        self.card = card
        self.player = player


normal_order = [ Value.SEVEN,
                Value.HEIGHT,
                Value.NINE,
                Value.JACK,
                Value.QUEEN,
                Value.KING,
                Value.TEN,
                Value.AS,
    ]

atout_order = [ Value.SEVEN,
                Value.HEIGHT,
                Value.QUEEN,
                Value.KING,
                Value.TEN,
                Value.AS,
                Value.NINE,
                Value.JACK,
    ]


class ComparabaleValue:

    def __init__(self,value,atout=False):
        self.value = value

        if atout:
            self.order = atout_order
        else:
            self.order = normal_order

        self.i1 = self.order.index(self.value)

    def __gt__(self, other):
        i2 = self.order.index(other)
        return self.i1>i2

    def __ge__(self, other):
        i2 = self.order.index(other)
        return self.i1>=i2

    def __lt__(self, other):
        i2 = self.order.index(other)
        return self.i1<i2

    def __le__(self, other):
        i2 = self.order.index(other)
        return self.i1<=i2

    def __eq__(self, other):
        i2 = self.order.index(other)
        return self.i1==i2

    def __ne__(self, other):
        return not(self.__eq__(other))


def trick_winner(trick,atout_color):
    if len(trick) == 0:
        raise ValueError(f" the trick is empty {trick}")


    main_color = trick[0].card.color

    main_color_cards_played = []
    atout_color_cards_played= []

    for card_played in trick:
        if card_played.card.color == main_color:
            main_color_cards_played.append(card_played)
        if card_played.card.color == atout_color:
            atout_color_cards_played.append(card_played)

    if len(atout_color_cards_played) > 0:
        values = []
        for card_played in atout_color_cards_played:
            values.append(ComparabaleValue(card_played.card.value,atout=True))

        winner = values.index(max(values)) ## arggh no arg max is python :( not very effective thow
        return atout_color_cards_played[winner].player

    elif len(main_color_cards_played) > 0:
        values = []
        for card_played in main_color_cards_played:
            values.append(ComparabaleValue(card_played.card.value,atout=False))

        winner = values.index(max(values)) ## arggh no arg max is python :( not very effective thow
        return main_color_cards_played[winner].player
    else:
        raise ValueError("we are missing some color here")
