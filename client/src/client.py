import socketio

sio = socketio.Client()



if __name__ == '__main__':
    sio.connect('http://localhost:8888')
    sio.emit('message', {'foo': 'bar'})
