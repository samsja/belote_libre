from game_class.game import Game
from game_class.rules import AbstractRule
from game_class.rules import basic_rules
from game_class.card import Color,Value,Card,CardPlayed
from game_class.trick import Trick
from game_class.hand import Hand

from game_class.comparable import ComparabaleValue,ComparabaleCard

from jsonifier import list_card_jsonify,trick_jsonify


g = Game(basic_rules,order_hands=False)

g.hands[0] = Hand([Card(Color.SPADE,Value.NINE),
          Card(Color.SPADE,Value.HEIGHT)],atout=Color.DIAMOND)

g.hands[1] = Hand([Card(Color.DIAMOND,Value.KING),
          Card(Color.DIAMOND,Value.HEIGHT)],atout=Color.DIAMOND)

g.hands[2] =  Hand([Card(Color.DIAMOND,Value.SEVEN),
          Card(Color.DIAMOND,Value.NINE)],atout=Color.DIAMOND)

g.play_a_card(g.hands[0][0],0)
g.play_a_card(g.hands[1][0],1)

print(g.play_a_card(g.hands[2][0],2))
