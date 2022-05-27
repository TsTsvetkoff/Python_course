import sys

from flask import Flask, request, render_template
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def gfg():
    available_chars = ["barbarian", "sorceress", "paladin"]
    if request.method == "POST":
        # getting input with name = fname in HTML form
        first_name = request.form.get("fname")
        # getting input with name = lname in HTML form
        last_name = request.form.get("lname").lower()
        if last_name in available_chars:
            return redirect(game_started())
        else:
            return redirect('/')
    return render_template("index.html")

@app.route('/game_started', methods=["GET", "POST"])
def game_started():

    return redirect('/game_started')




if __name__ == '__main__':
    app.run()