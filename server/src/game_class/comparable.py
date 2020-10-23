from game_class.card import Color,Value,Card


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


class ComparabaleCard:

    def __init__(self,card):
        if not(isinstance(card,Card)):
            raise TypeError(f"card should be a Card not a {type(card)}")

        self.card = card

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
