from agents import StupidPlayer,RandomPlayer
from game import SansAtout
from vizu import StdoutVizu



nb_pli = 10

env = SansAtout()
viz = StdoutVizu()
players = [ RandomPlayer() for _ in range(env.nb_player) ]


for _ in range(env.nb_player*nb_pli):

    action_passed = False

    while not(action_passed):
        possible_actions = env.get_cards_player(env.next_player)
        selected_action = players[env.next_player].select_an_action(possible_actions)
        action_passed = env.play_a_card(selected_action)


for pli in env.all_pli:
    print(viz.str_pli_info(pli))
