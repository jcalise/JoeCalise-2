from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = "SecretySecretSeccccccret"

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randrange(0, 101)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    guess = request.form['guess']
    print("Their guess", guess)

    try:
        guess = int(guess)

        if (guess == session['number']):
            session['result'] = "You got it right!"
            session['startover'] = True
        elif (guess > session['number']):
            session['result'] = "Too high!"
            session['startover'] = False
        elif (guess < session['number']):
            session['result'] = "Too low!"
            session['startover'] = False
    except:
        print("Entered a none numeric guess.")
        session['result'] = "That wasn't a number"
        session['startover'] = False
    return redirect('/')

@app.route('/startover')
def startover():
    session.pop('number')
    session.pop('result')
    session.pop('startover')
    return redirect('/')

app.run(debug=True)
