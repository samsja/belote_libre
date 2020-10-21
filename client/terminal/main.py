from unicards import unicard

import socketio
import json

import requests as r


host = "localhost:8888"

play = True


hand = r.get(f"http://{host}/hands/0")

print(hand.text)

sio = socketio.Client()


#sio.connect('http://localhost:8888')

#sio.emit('play', (0,0))



def show_card(color,value):
    str =  unicard(value+color, color=True)
    return str

print(show_card("s","A"))
