import socketio
import json
import requests as r
from handler import screen_clear,show_card
import json


host = "localhost:8888"

# sio = socketio.Client()
# sio.connect('http://localhost:8888')
# sio.emit('play', (0,0))


play = True

while play:
    screen_clear()
    hand = r.get(f"http://{host}/hands/0")

    hand_str = ""
    for card in hand.json():
        color = hand.json()[card]["color"]
        value = hand.json()[card]["value"]

        hand_str = hand_str  + show_card(color,value) + " "

    print(hand_str)




    print("\n \nq : quit \n")
    x = input()

    if x=="q":
        play = False
