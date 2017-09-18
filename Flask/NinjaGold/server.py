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

    if (building == "farm"):
        g = random.randrange(10,20)
        print("Going to the farm", g)
    elif (building == "cave"):
        print("Going to the cave!")
    elif (building == "house"):
        print("Going to the house!")
    elif (building == "casino"):
        print("Going to the casino!")

    if 'activities' not in session:
        session['activities'] = []

    session['activities'].append("You went to the " + building)

    print(session['activities'])
    return redirect('/')

@app.route('/clearall')
def clearall():
    session.pop('gold')
    session.pop('activities')
    return redirect('/')

app.run(debug=True)
