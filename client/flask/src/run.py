from flask import Flask, render_template
from handler import get_path_card
import requests as r

host = "localhost:8888"

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')





@app.route('/')
def home():
    return render_template('home.html')



@app.route('/play/<player_index>')
def play(player_index):


    try :
        hand = r.get(f"http://{host}/hands/{player_index}")
    except r.exceptions.HTTPError as errh:
        return f"Http Error:{errh}",500
    except r.exceptions.ConnectionError as errc:
        return f"Error Connecting:{errc}",500
    except r.exceptions.Timeout as errt:
        return f"Timeout Error:{errt}",500
    except r.exceptions.RequestException as err:
        return f"OOps: Something Else {err}",500


    Cards = []
    for card in hand.json():
        Cards.append(get_path_card(hand.json()[card]))


    try :
        trick = r.get(f"http://{host}/current_trick")
    except r.exceptions.HTTPError as errh:
        return f"Http Error:{errh}",500
    except r.exceptions.ConnectionError as errc:
        return f"Error Connecting:{errc}",500
    except r.exceptions.Timeout as errt:
        return f"Timeout Error:{errt}",500
    except r.exceptions.RequestException as err:
        return f"OOps: Something Else {err}",500



    trick_cards= ["" for i in range(4)]
    for key in trick.json().keys():
        card_played = trick.json()[key]
        player = card_played["player"]
        card = card_played["card"]
        trick_cards[player]=get_path_card(card)

    print(trick_cards)

    trick_str=[str((i-int(player_index))%4) for i in range(4)]
    print(trick_str)

    return render_template("hand.html", Cards = Cards, trick = trick_cards, len_trick=len(trick_cards),trick_str=trick_str,player=player_index)


if __name__ == '__main__':
    app.run(port=8000,debug=True)
