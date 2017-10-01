from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "Imsuperdupersecret"
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends) 

@app.route('/friends', methods=['POST'])
def create():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    email = request.form['email']
    if not EMAIL_REGEX.match(email):
        flash(u'Email is not valid', 'fail')
    else:
        flash(u'The email address you entered (' + email +') is a VALID email address. Thank you!', 'success')
        query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': email
        }
        mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit', methods=['POST'])
def edit(id):    
    query = "SELECT * FROM friends WHERE id =" + id
    friends = mysql.query_db(query)
    return render_template('edit.html', all_friends=friends)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    email = request.form['email']
    if not EMAIL_REGEX.match(email):
        flash(u'Email is not valid', 'fail')
    else:
        flash(u'The email address you entered (' + email +') is a VALID email address. Thank you!', 'success')
        query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = " + id
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': email
        }
        mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
