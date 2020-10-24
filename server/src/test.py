from game_class.game import Game
from game_class.rules import AbstractRule
from game_class.rules import basic_rules
from game_class.card import Color,Value,Card,CardPlayed
from game_class.trick import Trick
from game_class.hand import Hand

from game_class.comparable import ComparabaleValue,ComparabaleCard

from jsonifier import list_card_jsonify,trick_jsonify


g = Game(basic_rules)


h = Hand([Card(Color.SPADE,Value.AS),
          Card(Color.SPADE,Value.HEIGHT),
          Card(Color.SPADE,Value.NINE),
          Card(Color.SPADE,Value.KING)],atout=Color.DIAMOND)


little_hand = h._order_little_hand(h)

for card in little_hand:
    print(card.value)

h.order()


for card in h:
    print(card.value)

# tricks = []
# tricks.append(Trick([ CardPlayed(Card(Color.SPADE,Value.SEVEN),0),
#           CardPlayed(Card(Color.SPADE,Value.HEIGHT),1),
#           CardPlayed(Card(Color.SPADE,Value.NINE),2),
#           CardPlayed(Card(Color.SPADE,Value.TEN),3)
#         ]))
#
# tricks.append(Trick([ CardPlayed(Card(Color.DIAMOND,Value.SEVEN),0),
#           CardPlayed(Card(Color.DIAMOND,Value.HEIGHT),1),
#           CardPlayed(Card(Color.DIAMOND,Value.NINE),2),
#           CardPlayed(Card(Color.DIAMOND,Value.TEN),3)
#         ]))
#
# tricks.append(Trick([ CardPlayed(Card(Color.DIAMOND,Value.SEVEN),0),
#           CardPlayed(Card(Color.SPADE,Value.HEIGHT),1),
#           CardPlayed(Card(Color.SPADE,Value.NINE),2),
#           CardPlayed(Card(Color.SPADE,Value.TEN),3)
#         ]))
#
# tricks.append(Trick([ CardPlayed(Card(Color.DIAMOND,Value.SEVEN),0),
#           CardPlayed(Card(Color.SPADE,Value.HEIGHT),1),
#           CardPlayed(Card(Color.DIAMOND,Value.NINE),2),
#           CardPlayed(Card(Color.SPADE,Value.TEN),3)
#         ]))
#
# for trick in tricks:
#
#     print(trick.winner(atout_color=g.atout.color))
#
# tricks.append(Trick())
#
# print(len(tricks[-1]))
