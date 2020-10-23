from game_class.card import Color,Value,Card
from game_class.game import Game
from game_class.deck import Deck

import json
import copy






def  card_jsonify(card):
    if not(isinstance(card,Card)):
        raise TypeError(f"card should be a Card not a {type(card)}")

    return json.dumps(card, default=lambda card: card.__dict__)

def card_to_dict(card):
    card_dict = {}
    card_dict = copy.deepcopy(card.__dict__)
    card_dict["color"] = Color(card_dict["color"]).name
    card_dict["value"] = Value(card_dict["value"]).name

    return card_dict


def list_card_jsonify(deck):

    D = {}

    for i,card in enumerate(deck):
        D[i]=card_to_dict(card)

    return json.dumps(D)

def trick_jsonify(trick):

    D = {}
    card_played_dict = {}

    for i,card_played in enumerate(trick):
        card_played_dict["player"]=card_played.player
        card_played_dict["card"]=card_to_dict(card_played.card)
        D[i]=copy.deepcopy(card_played_dict)


    return json.dumps(D)
