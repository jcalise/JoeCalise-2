from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "Imsuperdupersecret"
mysql = MySQLConnector(app,'loginreg')
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    if 'loggedin' in session:
        query = "SELECT * FROM users WHERE id = " + str(session['id'])
        user = mysql.query_db(query)
        return render_template("index.html", user=user[0])
    else:
        return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    fname = request.form['first_name']
    lname = request.form['last_name']
    email = request.form['email']
    passw = request.form['pword']
    cpass = request.form['cpword']
    NAME_REGEX = re.compile(r'^[a-zA-Z]{3,}$')

    if len(passw) < 1 or len(cpass) < 1:
        flash(u'Password can not be blank!', 'fail')
    elif not NAME_REGEX.match(fname) or not NAME_REGEX.match(lname):
        flash(u'Names can only contain characters and must be at least 2 letters long!', 'fail')
    elif len(passw) < 8:
        flash(u'Password must be longer than 8 characters', 'fail')
    elif not EMAIL_REGEX.match(email):
        flash(u'Email is not valid', 'fail')
    elif passw != cpass:
        flash(u'Passwords do not match!', 'fail')
    else:
        hash_pw = bcrypt.generate_password_hash(passw)
        query = "INSERT INTO users (first_name, last_name, email, hash_pw, created_at, updated_at) VALUES (:first_name, :last_name, :email, :hash_pw, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': email,
            'hash_pw': hash_pw
        }
        user_id = mysql.query_db(query, data)
        if user_id is not 0:
            session['loggedin'] = True
            session['id'] = user_id
            flash(u'Registration Successful!!', 'success')
        else:
            flash(u'user creation failed', 'fail')

    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    passw = request.form['pword']

    if not EMAIL_REGEX.match(email):
        flash(u'Email is not valid', 'fail')

    if not len(passw) > 7:
        flash(u'Password is invalid', 'fail')

    if not '_flashes' in session:
        try:
            query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            data = { 'email': email }
            user = mysql.query_db(query, data)
            hashed_pw = user[0]['hash_pw']
            login_success = bcrypt.check_password_hash(hashed_pw, passw)
            flash(u'Login successful!', 'success')
        except:
            flash(u'Email or password were invalid', 'fail')
            login_success = False

        if login_success:
            session['id'] = user[0]['id']
            session['loggedin'] = True

    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')


app.run(debug=True)
