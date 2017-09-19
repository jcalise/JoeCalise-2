from flask import Flask, render_template, request, redirect, flash,session

app = Flask(__name__)
app.secret_key = "ItsaSECRET"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['post'])
def create_user():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    if len(name) < 1 or len(comment) < 1:
        flash("Name and/or Comment can not be blank!")
        return redirect('/')
    elif len(comment) > 120:
        flash("Comments can not be greater than 120 characters!")
        return redirect('/')
    else:
        return render_template("info.html", name=name, location=location, language=language, comment=comment)

app.run(debug=True)
