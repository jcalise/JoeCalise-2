from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = "Imsupersecret"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    if 'activities' not in session:
        session['activities'] = []
    activities = session['activities']

    if (building == "farm"):
        g = random.randrange(10,21)
        session['gold'] += g
        activities.append("You went to the " + building + " and earned " + str(g))
    elif (building == "cave"):
        g = random.randrange(5,11)
        session['gold'] += g
        activities.append("You went to the " + building + " and earned " + str(g))
    elif (building == "house"):
        g = random.randrange(2,6)
        session['gold'] += g
        activities.append("You went to the " + building + " and earned " + str(g))
    elif (building == "casino"):
        g = random.randrange(0,50)
        win = random.choice([True, False])
        if win:
            print("You won")
            session['gold'] += g
            activities.append("You went to the " + building + " and won " + str(g))
        else:
            print("You lost")
            session['gold'] -= g
            activities.append("You went to the " + building + " and lost " + str(g) + "! Ouch. :(")



    session['activities'] = activities

    return redirect('/')

@app.route('/clearall')
def clearall():
    session.pop('gold')
    session.pop('activities')
    return redirect('/')

app.run(debug=True)
