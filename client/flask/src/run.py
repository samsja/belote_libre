from flask import Flask, render_template

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



if __name__ == '__main__':
    app.run(port=8000,debug=True)
