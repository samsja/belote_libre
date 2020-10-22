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

@app.route('/hand/')
def hand():
    return render_template('hand.html')

@app.route('/play/<player>')
def play(player):


    try :
        hand = r.get(f"http://{host}/hands/{player}")
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
        color = hand.json()[card]["color"]
        value = hand.json()[card]["value"]

        Cards.append(get_path_card(color,value))
    print(hand.json())
    print(Cards)
    return render_template("hand.html", len = len(Cards), Cards = Cards)


if __name__ == '__main__':
    app.run(port=8000,debug=True)
