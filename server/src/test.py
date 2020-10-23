from game_class.game import Game
from game_class.rules import AbstractRule
from game_class.rules import basic_rules
from game_class.card import Color,Value,Card,trick_winner,CardPlayed
from game_class.trick import Trick
from game_class.comparable import ComparabaleValue

from jsonifier import list_card_jsonify,trick_jsonify


g = Game(basic_rules)

tricks = []
tricks.append(Trick([ CardPlayed(Card(Color.SPADE,Value.SEVEN),0),
          CardPlayed(Card(Color.SPADE,Value.HEIGHT),1),
          CardPlayed(Card(Color.SPADE,Value.NINE),2),
          CardPlayed(Card(Color.SPADE,Value.TEN),3)
        ]))

tricks.append(Trick([ CardPlayed(Card(Color.DIAMOND,Value.SEVEN),0),
          CardPlayed(Card(Color.DIAMOND,Value.HEIGHT),1),
          CardPlayed(Card(Color.DIAMOND,Value.NINE),2),
          CardPlayed(Card(Color.DIAMOND,Value.TEN),3)
        ]))

tricks.append(Trick([ CardPlayed(Card(Color.DIAMOND,Value.SEVEN),0),
          CardPlayed(Card(Color.SPADE,Value.HEIGHT),1),
          CardPlayed(Card(Color.SPADE,Value.NINE),2),
          CardPlayed(Card(Color.SPADE,Value.TEN),3)
        ]))

tricks.append(Trick([ CardPlayed(Card(Color.DIAMOND,Value.SEVEN),0),
          CardPlayed(Card(Color.SPADE,Value.HEIGHT),1),
          CardPlayed(Card(Color.DIAMOND,Value.NINE),2),
          CardPlayed(Card(Color.SPADE,Value.TEN),3)
        ]))

for trick in tricks:

    print(trick.winner(atout_color=g.atout.color))

tricks.append(Trick())

print(len(tricks[-1]))
