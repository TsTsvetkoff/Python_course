import sys

from flask import Flask, request, render_template
from werkzeug.utils import redirect

app = Flask(__name__)
first_action = 0
level_up_counter = 1

@app.route('/', methods=["GET", "POST"])
def gfg():
    available_chars = ["barbarian", "sorceress", "paladin"]
    if request.method == "POST":
        # getting input with name = fname in HTML form
        first_name = request.form.get("fname")
        # getting input with name = lname in HTML form
        last_name = request.form.get("lname").lower()
        if last_name in available_chars:
            return redirect('/game-started')
        else:
            return redirect('/')
    return render_template("index.html")

@app.route('/game-started', methods=["GET", "POST"])
def game_started():
    if request.method == "POST":
        begin = request.form.get("fname_1").lower()
        if begin == 'east':
            return redirect('/act-1')
        else:
            return redirect('/game-started')
    return render_template('game_started.html')

@app.route('/act-1', methods=["GET", "POST"])
def act_1():
    return render_template('act_1.html')



if __name__ == '__main__':
    app.run()