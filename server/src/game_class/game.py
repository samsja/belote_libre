from game_class.card import Color,Value,Card,CardPlayed
from game_class.deck import Deck
from game_class.trick import Trick
from game_class.hand import Hand


class Atout:

    def __init__(self,color=0):
        if color == None:
            self.color = None
        else:
            self.color = Color(color)





class Game:

    nb_trick = 8
    nb_card_hand= 8
    nb_player = 4

    def __init__(self,rules,atout = Atout(color=0),order_hands=True,first_player=0):
        """Init a Game
        Keyword arguments:
        rules -- a list of AbstractRule
        """

        self.rules = rules
        self.atout = atout
        self.order_hands = order_hands


        self.deck = Deck(shuffle=True)
        self.hands = [ Hand(self.deck[self.nb_card_hand*i:self.nb_card_hand*(i+1)]) for i in range(self.nb_player)]
        del self.deck
        self.do_order_hands()

        self.tricks = [Trick([])]

        self.first_player = first_player
        self.next_player = self.first_player
        self.over = False

    def do_order_hands(self):
        if self.order_hands:
            for hand in self.hands:
                hand.order(atout_color=self.atout.color)

    def validate_card(self,card,player):
        """Validate if a card could be play by the player
        Keyword arguments:
        card -- a Card instance
        player -- an int for the player index
        """

        if (not(isinstance(player,int)) or not(0<=player<self.nb_player)):
            raise TypeError(f"player should be an integer between 0 and {self.nb_player} not {type(player)}")

        if not(isinstance(card,Card)):
            raise TypeError(f"card should be a Card not {type(card)}")

        allowed = (card in self.hands[player]) and (self.next_player == player) and (not(self.over))

        if allowed and (len(self.tricks[-1])==self.nb_player or len(self.tricks[-1])==0 ):
            return True

        if not(allowed):
            return allowed

        for rule in self.rules:
            if not(rule.is_play_allowed(self,card,player)):
                allowed=False
                break

        if allowed:
            self.do_order_hands()

        return allowed

    def _trick_winner(self,trick):
        """determine which player won the trick
        Keyword arguments:
        trick -- a 4 long list of player_card
        """
        return trick_winner(trick,self.atout.color)

    def play_a_card(self,card,player):
        """A player play a card.
        Keyword arguments:
        card -- a Card instance
        player -- an int for the player index
        """

        if (not(isinstance(player,int)) or not(0<=player<self.nb_player)):
            raise TypeError(f"player should be an integer between 0 and {self.nb_player} not {type(player)}")

        if not(isinstance(card,Card)):
            raise TypeError(f"card should be a Card not {type(card)}")



        if self.validate_card(card,player) :
            if len(self.tricks[-1]) == self.nb_player:

                print(len(self.tricks[-1]),len(self.tricks))
                new_empty_trick = Trick([])
                print(f"new empty trick lenght {len(new_empty_trick)}")
                self.tricks.append(new_empty_trick)
                print(len(self.tricks[-1]),len(self.tricks))

            self.hands[player].remove(card)
            self.tricks[-1].append(CardPlayed(card,player))

            if len(self.tricks[-1]) == self.nb_player:
                self.next_player = self.tricks[-1].winner(atout_color=self.atout.color)
            else:
                self.next_player = self._rotate_player(self.next_player)

            if len(self.tricks)>=self.nb_trick and len(self.tricks[-1])==self.nb_player:
                self.over = True

            return True
        else:
            return False

    def compute_points(self):

        team_1_points = 0
        team_2_points = 0


        for i,trick in enumerate(self.tricks):

            if trick.set != []:
                winner = trick.winner(self.atout.color)

                trick_points = trick.total_value(self.atout.color)
                if i >=self.nb_trick: # dix de der
                    trick_points += 10

                if winner in [0,2]:
                    team_1_points += trick_points
                elif winner in [1,3]:
                    team_2_points += trick_points
                else:
                    raise ValueError("winner should be in [0,1,2,3]")

        return team_1_points,team_2_points

    def reinit_game(self):
        self.__init__(self.rules,atout = self.atout,order_hands=self.order_hands,first_player=self._rotate_player(self.first_player))


    @staticmethod
    def get_co_player(player):
        if (not(isinstance(player,int)) or not(0<=player<Game.nb_player)):
            raise TypeError(f"player should be an integer between 0 and {Game.nb_player} not {type(player)}")

        return (player+2)%Game.nb_player

    @staticmethod
    def _rotate_player(player):

        return (player +1)%Game.nb_player
