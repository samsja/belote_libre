from deck import Value,Color,map_unicard_value,map_unicard_colors
from unicards import unicard


class StdoutVizu:
    # def __init__(self):
    #
    #
    def card_info(self,card,print_b=True):
        str =  f" {Value(card[0]).name} of {Color(card[1]).name} "

        if print_b:
            print(str)

        return str

    def set_info(self,set,print_b=True):

        str = f"The set has {len(set)} cards \n"

        for idx, card in enumerate(set):
            str = str + f"{idx + 1}. " +  self.card_info(card,print_b=False) + "\n"

        if print_b:
            print(str)

        return str

    def pli_info(self,pli,print_b=True):
        str = f"The pli has {len(pli)} cards \n"
        for idx, card in enumerate(pli):
            str = str + f"{idx + 1}.  {self.card_info(card[0],print_b=False)} play by {card[1]} \n"

        if print_b:
            print(str)

        return str







class TerminalVizu:

    def card_info(self,card,print_b=True):

        val = int(Value(card[0]).value)
        color = int(Color(card[1]).value)

        str =  unicard(map_unicard_value[val]+map_unicard_colors[color], color=True)

        if print_b:
            print(str)

        return str

    def set_info(self,set,print_b=True):

        str = f"The set has {len(set)} cards \n"

        for idx, card in enumerate(set):
            str = str + f"{idx + 1}. " +  self.card_info(card,print_b=False) + "\n"

        if print_b:
            print(str)

        return str

    def pli_info(self,pli,print_b=True):
        if len(pli) != 4:
            raise ValueError("only 4 players allowed for terminal card")

        cards = [ card[0] for card in pli]
        idx = [ card[1] for card in pli]


        print(f" {self.card_info(cards[idx.index(0)],print_b=False)} ")
        print(f"{self.card_info(cards[idx.index(1)],print_b=False)} {self.card_info(cards[idx.index(2)],print_b=False)}   ")
        print(f" {self.card_info(cards[idx.index(3)],print_b=False)} ")
