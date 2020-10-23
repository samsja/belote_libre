from game_class.card import Color,Value,Card
from game_class.comparable import ComparabaleValue


class AbstractRule:

    def __init__(self):
        pass

    def is_play_allowed(self,game,card,player):
        if not(isinstance(player,int)):
            raise TypeError(f"player should be an integer not {type(player)}")

        if not(isinstance(card,Card)):
            raise TypeError(f"card should be a Card not {type(card)}")

        return True


class StupidRule(AbstractRule):

    def is_play_allowed(self,game,card,player):
        super().is_play_allowed(game,card,player)
        return False


class BasicColorRule(AbstractRule):

    def is_play_allowed(self,game,card,player):
        super().is_play_allowed(game,card,player)

        main_color = game.tricks[-1][0].card.color

        if card.color != main_color:

            if (game.tricks[-1].winner(atout_color=game.atout.color) == game.get_co_player(player)) and (main_color != game.atout):
                # allow "pisser" when co player is master
                return True

            had_main_color = False
            had_atout = False
            for card_in_hand in game.hands[player]:
                if card_in_hand.color == main_color:
                    had_main_color = True
                if card_in_hand.color == game.atout.color:
                    had_atout = True

            if had_main_color:
                return False
            elif had_atout and (card.color != game.atout.color) :
                return False
            else:
                return True

        else:
            return True

class GoUpAtout(AbstractRule):

    def is_play_allowed(self,game,card,player):
        super().is_play_allowed(game,card,player)

        main_color = game.tricks[-1][0].card.color

        if main_color == game.atout.color:

            has_better= False
            for card_in_hand in game.hands[player]:
                if (card_in_hand.color == game.atout.color) and (ComparabaleValue(card_in_hand.value,atout=True)>game.tricks[-1][-1].card.value) :
                    has_better = True
                    break
            if has_better:
                return ComparabaleValue(card.value,atout=True) > game.tricks[-1][-1].card.value
            else:
                return True
        else:
            return True



basic_rules = [AbstractRule(),BasicColorRule(),GoUpAtout()]
