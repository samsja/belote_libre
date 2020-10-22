import socketio
import json
import requests as r
from handler import screen_clear,show_card
import json
import sys

host = "localhost:8888"

sio = socketio.Client()
sio.connect(f'http://{host}')


stop = False

debug = False

if len(sys.argv) >= 2:
    player_index = int(sys.argv[1])
else:
    player_index = 0





def play():

    hand = r.get(f"http://{host}/hands/{player_index}")

    print( f"You are player {player_index}")
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

    if x=="q":
        sio.disconnect()

    elif x in range(1,9):

        response = r.post(f"http://{host}/is_play_allowed/{player_index}",json={'card': x-1})
        if response.json()["result"]:
            sio.emit('play', (x-1,player_index))
        else:
            if not(debug):
                screen_clear()
            print("you are not able to play that card try again")
            play()


    else:
        if not(debug):
            screen_clear()

        print("no play have been submitted")
        play()

@sio.on('played')
def on_play_allowed(data):
    if not(debug):
        screen_clear()

    data = json.loads(data)

    if data["played"]:
        player = data["player"]
        card_played = data["card_played"]

        if int(player)==player_index:
            print(f"you play {card_played}")
        else:
            print(f"player {player} play {card_played}")

    play()


play()
