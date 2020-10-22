import flask
import flask_socketio as socket


from game_class.game import Game
from jsonifier import list_card_jsonify
import json


# Init the server
app = flask.Flask(__name__)
socketio = socket.SocketIO(app, logger=True)

g = Game()

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

@app.route("/is_play_allowed/<player>",methods = ['POST'])
def is_play_allowed(player):

    data = flask.request.json

    player = int(player)
    is_allowed = {"result":g._validate_card(g.hands[player][data["card"]],player)}
    json_result = json.dumps(is_allowed)

    response = app.response_class(
        response=json_result,
        mimetype='application/json'
    )
    return response

@app.route("/table/")
def get_table():
    str = ""

    for i,trick in enumerate(g.tricks):
        str = str + f"trick {i}\n"

        for card_played in trick:
            str = str + f"\n{card_played.player} play {card_played.card}\n"

    return str



@socketio.on('play')
def handle_play(card_index,player):
    play_allowed = g.play_a_card(g.hands[int(player)][int(card_index)],int(player))


    print(f"card_index:{card_index}, player: {player}, allowed: {play_allowed}")

    socketio.emit("play_allowed",play_allowed)


if __name__ == '__main__':
    """ Run the app. """
    socketio.run(app, port=8888, debug=True)
