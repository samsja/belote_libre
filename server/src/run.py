import flask
import flask_socketio as socket
from flask_cors import CORS

from game_class.game import Game
from game_class.rules import basic_rules

from jsonifier import list_card_jsonify,trick_jsonify
import json


# Init the server
app = flask.Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

socketio = socket.SocketIO(app, cors_allowed_origins="*",logger=True)

g = Game(basic_rules)

@app.route('/')
def root():
    return "BWC (Belote World Championship) belt! API"

@app.route("/hands/<player>")
def get_hands(player):
    response = app.response_class(
        response=list_card_jsonify(g.hands[int(player)]),
        mimetype='application/json'
    )
    return response

@app.route("/current_trick")
def get_current_trick():

    trick = g.tricks[-1]
    response = app.response_class(
        response=trick_jsonify(trick),
        mimetype='application/json'
    )
    return response


@app.route("/is_play_allowed/<player>",methods = ['POST'])
def is_play_allowed(player):

    data = flask.request.json

    player = int(player)
    is_allowed = {"result":g.validate_card(g.hands[player][data["card"]],player)}
    json_result = json.dumps(is_allowed)

    response = app.response_class(
        response=json_result,
        mimetype='application/json'
    )
    return response


@socketio.on('play')
def handle_play(card_index,player):
    play_allowed = g.play_a_card(g.hands[int(player)][int(card_index)],int(player))

    response = {
                "player":player,
                "card_played"  :card_index,
                "played": play_allowed
               }

    socketio.emit("played",json.dumps(response))


if __name__ == '__main__':
    """ Run the app. """
    socketio.run(app, port=8888, debug=True)
