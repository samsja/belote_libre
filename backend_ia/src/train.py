from agents import StupidPlayer,RandomPlayer
from game import SansAtout
from vizu import StdoutVizu,TerminalVizu



nb_pli = 8

env = SansAtout()
# viz = StdoutVizu()
viz = TerminalVizu()

players = [ RandomPlayer() for _ in range(env.nb_player) ]


for i in range(env.nb_player*nb_pli):

    print(i)

    action_passed = False

    while not(action_passed):
        possible_actions = env.get_cards_player(env.next_player)
        selected_action = players[env.next_player].select_an_action(possible_actions)
        action_passed = env.play_a_card(selected_action)



for idx,pli in enumerate(env.all_pli):
    print(f"{idx+1}.")
    viz.pli_info(pli)
