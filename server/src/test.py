from game_class.game import Game
from game_class.rules import AbstractRule
from game_class.rules import basic_rules
from game_class.card import Color,Value,Card,CardPlayed
from game_class.trick import Trick
from game_class.hand import Hand
from game_class.comparable import ComparabaleValue,ComparabaleCard
from game_class.coinche import Coinche

from jsonifier import list_card_jsonify,trick_jsonify


c = Coinche(basic_rules)
print(c.play_a_bet("coinche",Color.DIAMOND,0))

print(c.play_a_bet(0,Color.DIAMOND,0))
print(c.play_a_bet(80,Color.DIAMOND,0))
print(c.play_a_bet(80,Color.DIAMOND,0))
print(c.play_a_bet(80,Color.DIAMOND,1))
print(c.play_a_bet(90,Color.DIAMOND,1))
print(c.play_a_bet(250,Color.DIAMOND,2))
print(c.play_a_bet("coinche",Color.DIAMOND,3))
