from flask import Flask, request, render_template
from werkzeug.utils import redirect

app = Flask(__name__, template_folder='templates')
first_action = 0
level_up_counter = 1
first_name = None
last_name = None
level = 1


@app.route('/', methods=["GET", "POST"])
def gfg():
    available_chars = ["barbarian", "sorceress", "paladin"]
    if request.method == "POST":
        global first_name, last_name
        # getting input with name = fname in HTML form
        first_name = request.form.get("fname")
        # getting input with name = lname in HTML form
        last_name = request.form.get("lname").lower()
        if last_name in available_chars:
            return redirect('/game-started')
        else:
            return redirect('/')
    return render_template("index.html")


@app.context_processor
def context_process():
    return dict(char_name=first_name, char_type=last_name, char_level=level)


@app.route('/game-started', methods=["GET", "POST"])
def game_started():
    if request.method == "POST":
        begin = request.form.get("fname_1").lower()
        if begin == 'east':
            return redirect('/blood-moor')
        else:
            return redirect('/game-started')
    return render_template('game_started.html')


@app.route('/blood-moor', methods=["GET", "POST"])
def blood_moor():
    global first_name, last_name, level
    level += 1
    if request.method == "POST":
        begin1 = request.form.get("fname_2")
        print(begin1)
        if begin1 == '1':
            return redirect('/dungeon-den')
        if begin1 == "2":
            return redirect('/cold-plants')
        else:
            return redirect('/blood-moor')
    return render_template('blood_moor.html')


@app.route('/dungeon-den', methods=["GET", "POST"])
def den():
    return render_template('dungeon_den.html')


@app.route('/cold-plants', methods=["GET", "POST"])
def cold_plants():
    return render_template('cold_plants.html')


if __name__ == '__main__':
    app.run()