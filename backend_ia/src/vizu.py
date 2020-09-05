from deck import Value,Color



class stdout_vizu:
    # def __init__(self):
    #
    #
    def str_card_info(self,card):
        return f" {Value(card[0]).name} of {Color(card[1]).name} "


    def str_set_info(self,set):

        str = f"The set has {len(set)} cards \n"

        for idx, card in enumerate(set):
            str = str + f"{idx + 1}. " +  self.str_card_info(card) + "\n"

        return str

    def str_pli_info(self,pli):
        str = f"The pli has {len(pli)} cards \n"
        for idx, card in enumerate(pli):
            str = str + f"{idx + 1}.  {self.str_card_info(card[0])} play by {card[1]} \n"
        return str
