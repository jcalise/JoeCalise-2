from flask import Flask, render_template, redirect, session, request, flash
import re

app = Flask(__name__)
app.secret_key = "Imsupersecret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    passw = request.form['pass']
    cpass = request.form['cpass']
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    NAME_REGEX = re.compile(r'^[a-zA-Z\.\+_-]*$')


    if len(fname) < 1 or len(lname) < 1 or len(email) < 1 or len(passw) < 1 or len(cpass) < 1:
        flash(u'Fields can not be blank!', 'error')
    elif not NAME_REGEX.match(fname) or not NAME_REGEX.match(lname):
        flash(u'Names can not contain numbers!', 'error')
    elif len(passw) < 8:
        flash(u'Password must be longer than 8 characters', 'error')
    elif not EMAIL_REGEX.match(email):
        flash(u'Email is not valid', 'error')
    elif passw != cpass:
        flash(u'Passwords do not match!', 'error')
    else:
        flash(u'SUCCESS!', 'success')


    return redirect('/')

app.run(debug=True)
