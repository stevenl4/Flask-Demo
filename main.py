from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<username>')
def index(username=None):
    return render_template('user.html', username=username)


@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return 'You are using POST'
    else:
        return 'You are using GET'


@app.route("/shopping")
def shopping():
    food = ["Cheese", "Tuna", "Beef"]
    return render_template("shopping.html", food=food)


@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good</h2>'


@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", username=username)





if __name__ == '__main__':
    app.run(debug=True)
