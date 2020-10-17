import socketio
import json

sio = socketio.Client()


sio.connect('http://localhost:8888')

sio.emit('play', (0,0))
