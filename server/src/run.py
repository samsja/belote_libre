import flask
import flask_socketio as socket
from flask_cors import CORS

from game_class.game import Game
from game_class.card import Color

from game_class.coinche import Coinche
from game_class.rules import basic_rules

from jsonifier import list_card_jsonify,trick_jsonify,bets_jsonify
import json


# Init the server
app = flask.Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

socketio = socket.SocketIO(app, cors_allowed_origins="*",logger=True)


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
        response=list_card_jsonify(coinche.game.hands[int(player)]),
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
    trick = coinche.game.tricks[-1]
    response = app.response_class(
        response=trick_jsonify(trick),
        mimetype='application/json'
    )
    return response


@app.route("/current_bets")
def get_current_bets():
    """Return the current trick

    Return Statement:
    json with the trick:

    """
    bets = coinche.bets
    response = app.response_class(
        response=bets_jsonify(bets),
        mimetype='application/json'
    )
    return response


@app.route("/game_info")
def game_info():
    """Return some info on the current game
    Return Statement:
    json with some game info:
    """

    team_1_points,team_2_points = coinche.game.compute_points()
    info = { "next_player": coinche.game.next_player,
             "atout": Color(coinche.game.atout.color).name,
             "team_1_points": team_1_points,
             "team_2_points": team_2_points
           }

    response = app.response_class(
        response=json.dumps(info),
        mimetype='application/json'
    )
    return response

@app.route("/players_name/<player>")
def players_name(player):
    """Return info on the current game
    Return Statement:
    json with players name:
    """

    names = ["south","west","north","est"]
    names_info = [ names[(i+int(player))%4] for i in range(len(names))]

    response = app.response_class(
        response=json.dumps(names_info),
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

    is_allowed = coinche.betting_phase_over and coinche.game.validate_card(coinche.game.hands[player][data["card"]],player)
    is_allowed_dict = {"result":is_allowed}

    print(data,is_allowed_dict)

    response = app.response_class(
        response=json.dumps(is_allowed_dict),
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

    value = data["value"]
    if not(value in ["pass","coinche"]):
        value = int(data["value"])


    is_allowed = coinche.play_a_bet(value,Color[data["color"]],player,add=False)
    is_allowed_dict = {"result":is_allowed}

    print(data,is_allowed_dict)

    response = app.response_class(
        response=json.dumps(is_allowed_dict),
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
    play_allowed = coinche.game.play_a_card(coinche.game.hands[int(player)][int(card_index)],int(player))
    print(card_index,player,play_allowed)


    response = {
                "player":player,
                "card_played"  :card_index,
                "played": play_allowed
               }

    socketio.emit("played",json.dumps(response))

    if coinche.game.over:
        team_1_points,team_2_points = coinche.game.compute_points()
        response = {
                    "team_1_points" :  team_1_points,
                    "team_2_points" :   team_2_points
                   }
        socketio.emit("game_over",json.dumps(response))




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
    value = bet["value"]
    if not(value in ["pass","coinche"]):
        value = int(bet["value"])
    bet_allowed = coinche.play_a_bet(value,Color[bet["color"]],player)
    player = int(player)

    print(bet,bet_allowed)

    response = {
                "player":player,
                "bet"  :bet,
                "played": bet_allowed,
                "has_game_start":coinche.betting_phase_over,
                "game_atout":coinche.game.atout.color.name
               }

    socketio.emit("new_bet",json.dumps(response))



if __name__ == '__main__':
    """ Run the app. """
    socketio.run(app, host='0.0.0.0' ,port=8888, debug=True)
