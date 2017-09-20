from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    ninjas = ["donatello","leonardo","michelangelo","raphael"]
    return render_template("ninja.html", ninjas=ninjas)

@app.route('/ninja/<color>')
def ninjas(color):
    ninjas = {
        'orange':'michelangelo',
        'blue':'leonardo',
        'red':'raphael',
        'purple':'donatello'
    }

    if color in ninjas:
        ninja = [ninjas[color]]
    else:
        ninja = ['notapril']
    return render_template("ninja.html", ninjas=ninja)

app.run(debug=True)
