from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "Imsuperdupersecret"
mysql = MySQLConnector(app,'thewall')
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
POST_REGEX = re.compile(r'^[\w\s\,\'\"_.!?-]*$')

@app.route('/')
def index():
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
        query = "INSERT INTO users (first_name, last_name, email, pass, created_at, updated_at) VALUES (:first_name, :last_name, :email, :hash_pw, NOW(), NOW())"
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
            return redirect('/thewall')
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
            hashed_pw = user[0]['pass']
            login_success = bcrypt.check_password_hash(hashed_pw, passw)
            flash(u'Login successful!', 'success')
        except:
            flash(u'Email or password were invalid', 'fail')
            login_success = False

        if login_success:
            session['id'] = user[0]['id']
            session['loggedin'] = True
            return redirect('/thewall')

    return redirect('/')

@app.route('/thewall')
def thewall():
    query = "SELECT * FROM users WHERE id = " + str(session['id'])
    user = mysql.query_db(query)

    query = "SELECT messages.message, messages.id, first_name, last_name, messages.created_at FROM messages\
            JOIN users on messages.user_id=users.id"
    posts = mysql.query_db(query)

    get_comments_query = "SELECT comments.comment, message_id, comments.created_at, first_name, last_name FROM comments\
                          JOIN messages ON messages.id=comments.message_id\
                          JOIN users ON users.id=comments.user_id"
    comments = mysql.query_db(get_comments_query)

    return render_template("thewall.html", user=user[0], posts=posts, comments=comments)

@app.route('/message', methods=['POST'])
def post_message():
    message = request.form['message']
    uid = request.form['id']
    
    print message, uid
    if not POST_REGEX.match(message):
        flash(u'Your message contains invalid characters, only puncuation allowed.', 'fail')
    
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:uid, :message, NOW(), NOW())"
    data = {
        'uid': uid,
        'message': message
    }
    mysql.query_db(query, data)
    return redirect('/thewall')

@app.route('/post_comment/<message_id>', methods=['POST'])
def post_comment(message_id):
    comment = request.form['comment']

    if not POST_REGEX.match(comment):
        flash(u'Your comment contains invalid characters, only puncuation allowed.', 'fail')
    else:
        query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at)\
                         VALUES (:user_id, :message_id, :comment, NOW(), NOW())"
        data = {
            "user_id": session['id'],
            "message_id": message_id,
            "comment": request.form["comment"]
        }
        mysql.query_db(query, data)
    return redirect('/thewall')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

app.run(debug=True)
