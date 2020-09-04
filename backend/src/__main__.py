from game import PliBasedGame,RulesException
from deck import BeloteDeck



def play(game):
    continued = True

    while continued:
        player = int(input("what player: "))
        card = int(input("what card: "))

        game.play(card,player)

        print(f"player {player} has played : {game.deck.set[card]}")



p = PliBasedGame(BeloteDeck(),4)
play(p)
