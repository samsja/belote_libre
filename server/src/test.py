from game_class.game import Game
from jsonifier import list_card_jsonify,trick_jsonify

g = Game()
g.play_a_card(g.hands[0][0],0)

print(trick_jsonify(g.tricks[-1]))
