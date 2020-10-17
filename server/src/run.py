import flask
import flask_socketio as socket


# Init the server
app = flask.Flask(__name__)
socketio = socket.SocketIO(app, logger=True)

@app.route('/')
def root():
    return "Hello world!"


@socketio.on('message')
def handle_message(message):
    print(f"received message:{message}")


if __name__ == '__main__':
    """ Run the app. """
    socketio.run(app, port=8888, debug=True)
