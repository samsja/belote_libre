import flask
import flask_socketio as socket

from game_class.game import Game
from jsonifier import list_card_jsonify


# Init the server
app = flask.Flask(__name__)
socketio = socket.SocketIO(app, logger=True)

g = Game()

@app.route('/')
def root():
    return "BWC (Belote World Championship) belt!"

@app.route("/hands/<player>")
def get_hands(player):
    response = app.response_class(
        response=list_card_jsonify(g.hands[int(player)]),
        mimetype='application/json'
    )
    return response
@socketio.on('message')
def handle_message(message):
    print(f"received message:{message}")


if __name__ == '__main__':
    """ Run the app. """
    socketio.run(app, port=8888, debug=True)
