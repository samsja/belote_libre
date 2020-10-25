import flask
import flask_socketio as socket
from flask_cors import CORS

from game_class.game import Game
from game_class.card import Color

from game_class.coinche import Coinche
from game_class.rules import basic_rules

from jsonifier import list_card_jsonify,trick_jsonify
import json


# Init the server
app = flask.Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

socketio = socket.SocketIO(app, cors_allowed_origins="*",logger=True)

g = Game(basic_rules)
coinche = Coinche(basic_rules)

@app.route('/')
def root():
    return "BWC (Belote World Championship) belt! API"

@app.route("/hands/<player>")
def get_hands(player):
    """Return hand of the player <player>

    Keyword arguments:
    player -- an int for the player index

    Return Statement:
    json with the hand
    ex : {
      "0": {
        "color": "SPADE",
        "value": "AS"
          },
     ...
      "7": {
        "color": "DIAMOND",
        "value": "KING"
      }
    }
    """
    response = app.response_class(
        response=list_card_jsonify(g.hands[int(player)]),
        mimetype='application/json'
    )
    return response

@app.route("/current_trick")
def get_current_trick():
    """Return the current trick

    Return Statement:
    json with the trick:
    ex :
    {
      "0": {
        "player": 0,
        "card": {
          "color": "HEART",
          "value": "AS"
        }
      },
      "1": {
        "player": 1,
        "card": {
          "color": "HEART",
          "value": "JACK"
        }
      }
    }
    """
    trick = g.tricks[-1]
    response = app.response_class(
        response=trick_jsonify(trick),
        mimetype='application/json'
    )
    return response


@app.route("/is_play_allowed/<player>",methods = ['POST'])
def is_play_allowed(player):
    """Return if a play is allowed
    POST argument:
    ex :
    {
        "value": "SEVEN",
        "color": "DIAMOND"
    }

    Return Statement:
    json  ex : {"result",bool} if the play is allowed
    """
    data = flask.request.json

    player = int(player)
    is_allowed = {"result":g.validate_card(g.hands[player][data["card"]],player)}
    json_result = json.dumps(is_allowed)

    response = app.response_class(
        response=json_result,
        mimetype='application/json'
    )
    return response

@app.route("/is_bet_allowed/<player>",methods = ['POST'])
def is_bet_allowed(player):
    """Return if a bet is allowed
    POST argument:
    ex :
    {
        "value": 80,
        "color": "DIAMOND"
    }


    Return Statement:
    json  ex : {"result",bool} if the bet is allowed
    """
    data = flask.request.json

    player = int(player)
    is_allowed = {"result":coinche.play_a_bet(int(data["value"]),Color[data["color"]],player,add=False)}
    json_result = json.dumps(is_allowed)

    response = app.response_class(
        response=json_result,
        mimetype='application/json'
    )
    return response

@socketio.on('play')
def handle_play(card_index,player):
    """Play the desire card
    Keyword arguments:
    card_index : int
    player : int

    Return Statement:{
                "player":player,
                "card_played"  :card_index,
                "played": play_allowed
               }

    """
    play_allowed = g.play_a_card(g.hands[int(player)][int(card_index)],int(player))

    response = {
                "player":player,
                "card_played"  :card_index,
                "played": play_allowed
               }

    socketio.emit("played",json.dumps(response))

@socketio.on('bet')
def handle_bet(bet,player):
    """Play the desire card
    Keyword arguments:
    bet : json  : ex     {
            "value": 80,
            "color": "DIAMOND"
        }
    player : int

    Return Statement {
                "player":player,
                "bet"  :bet,
                "played": bet_allowed

               }
    """
    bet = json.loads(bet)
    bet_allowed = coinche.play_a_bet(int(data["value"]),Color[data["color"]],player)

    response = {
                "player":player,
                "bet"  :bet,
                "played": bet_allowed

               }
    socketio.emit("bet",json.dumps(response))

if __name__ == '__main__':
    """ Run the app. """
    socketio.run(app, port=8888, debug=True)
