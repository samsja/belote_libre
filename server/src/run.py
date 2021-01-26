import flask
import flask_socketio as socket
from flask_cors import CORS

from game_class.game import Game, Atout
from game_class.card import Color

from game_class.coinche import Coinche
from game_class.rules import basic_rules

from jsonifier import list_card_jsonify,trick_jsonify,bets_jsonify
import json
from utils import short_uuid
import config

# Init the server
app = flask.Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

socketio = socket.SocketIO(app, cors_allowed_origins="*",logger=True)



coinches = {"init":Coinche(basic_rules) }
#coinches = {"init":Coinche([]) }

coinches["init"].betting_phase_over = True
 


@app.route('/')
def alive():
    """Health check.
    """
    return flask.jsonify({"alive": True})


@app.route('/create_room')
def create_room():
    """Create an instance of the game
    Return Statement:
    json with the hand
    ex : { "uuid":c6892d47}
    """
    if len(coinches)<config.MAX_GAMES:
        coinche = Coinche(basic_rules)

        uuid = short_uuid()

        coinches[uuid]=coinche


        return flask.jsonify({"uuid": uuid})
    else:
        return 'Oops ,too many coinches already created', 409




@app.route('/reinit_game')
def reinit_game():
    """Reinit the game
    """

    #coinches["init"].reinit()
    del coinches["init"]

    coinches["init"]= Coinche(basic_rules) 

    coinches["init"].betting_phase_over = True
     
   
    socketio.emit("game_reset")

    return flask.jsonify({"done": True})





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
        response=list_card_jsonify(coinches["init"].game.hands[int(player)]),
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
    trick = coinches["init"].game.tricks[-1]
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
    bets = coinches["init"].bets
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

    team_1_points,team_2_points = coinches["init"].game.compute_points()

    if coinches["init"].betting_phase_over:
        next_player = coinches["init"].game.next_player
    else:
        next_player =  coinches["init"].next_player


    info = {
             "next_player": next_player,
             "betting_phase_over" : coinches["init"].betting_phase_over,
             "atout": Color(coinches["init"].game.atout.color).name,
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
    # names_info = [ names[(i+int(player))%4] for i in range(len(names))]
    names[int(player)]="you"

    response = app.response_class(
        response=json.dumps(names),
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

    is_allowed = coinches["init"].betting_phase_over 
    
    if not(is_allowed):
        print(f"{data} betting_phase_not_over")    
    else :
        is_allowed = is_allowed and coinches["init"].game.validate_card(coinches["init"].game.hands[player][data["card"]],player)
         
        if not(is_allowed):
            print(f"{data} card not valid")    
        
    



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


    is_allowed = coinches["init"].play_a_bet(value,Color[data["color"]],player,add=False)
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
    play_allowed = coinches["init"].game.play_a_card(coinches["init"].game.hands[int(player)][int(card_index)],int(player))
    print(card_index,player,play_allowed)


    response = {
                "player":player,
                "card_played"  :card_index,
                "played": play_allowed
               }

    socketio.emit("played",json.dumps(response))

    if coinches["init"].game.over:
        team_1_points,team_2_points = coinches["init"].game.compute_points()
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
    bet_allowed = coinches["init"].play_a_bet(value,Color[bet["color"]],player)
    player = int(player)

    print(bet,bet_allowed)

    response = {
                "player":player,
                "bet"  :bet,
                "played": bet_allowed,
                "has_game_start":coinches["init"].betting_phase_over,
                "game_atout":coinches["init"].game.atout.color.name
               }

    socketio.emit("new_bet",json.dumps(response))


@socketio.on('change_atout')
def change_atout(atout_color,player):
   

    coinches["init"].game.atout = Atout() 
    coinches["init"].game.atout.color = Color[atout_color] 
    coinches["init"].game.do_order_hands() 


    response = {
                "atout_updated":True
                }

    socketio.emit("atout_changed",json.dumps(response))



if __name__ == '__main__':
""" Run the app. """
    socketio.run(app, host='0.0.0.0' ,port=8888, debug=True)
