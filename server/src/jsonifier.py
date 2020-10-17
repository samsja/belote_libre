from game_class.card import Color,Value,Card
from game_class.game import Game
from game_class.deck import Deck

import json







def  card_jsonify(card):
    if not(isinstance(card,Card)):
        raise TypeError(f"card should be a Card not a {type(card)}")

    return json.dumps(card, default=lambda card: card.__dict__)

def list_card_jsonify(deck):
    D = {}

    for i,card in enumerate(deck):
        card_dict = card.__dict__
        card_dict["color"] = Color(card_dict["color"]).name
        card_dict["value"] = Value(card_dict["value"]).name

        D[i]=card_dict

    return json.dumps(D)
