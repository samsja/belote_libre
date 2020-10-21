import socketio
import json
import requests as r
from handler import screen_clear,show_card
import json


host = "localhost:8888"

sio = socketio.Client()
sio.connect('http://localhost:8888')


stop = False

debug = True

player_index = 0

while not(stop):

    if not(debug):
        screen_clear()


    hand = r.get(f"http://{host}/hands/{player_index}")

    hand_str = ""
    for card in hand.json():
        color = hand.json()[card]["color"]
        value = hand.json()[card]["value"]

        hand_str = hand_str  + show_card(color,value) + " "

    print(hand_str)

    print("\n \nplay k-th cards")
    x = input()

    try :
        x = int(x)
    except ValueError:
        pass

    # if x=="q":
    #     print("here")
    #     stop = True

    if x in range(1,9):
        print(sio.emit('play', (x-1,player_index)))
