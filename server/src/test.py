from game_class.game import Game
from jsonifier import list_card_jsonify,trick_jsonify

g = Game()

i = 0
while  g.play_a_card(g.hands[i][0],i):
    i = (i+1)%4
    if len(g.hands[i]) == 0:
        break

print(len(g.tricks))
