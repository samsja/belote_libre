from game_class.game import Game
from game_class.rules import AbstractRule
from game_class.rules import basic_rules
from game_class.card import Color,Value,Card,is_better,ComparabaleValue

from jsonifier import list_card_jsonify,trick_jsonify


g = Game(basic_rules)

r = AbstractRule()
