from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "Imsuperdupersecret"
mysql = MySQLConnector(app,'emails')


@app.route('/')
def index():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('index.html', all_emails=emails) 

@app.route('/email', methods=["POST"])
def add():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    email = request.form['email']
    if not EMAIL_REGEX.match(email):
        flash(u'Email is not valid', 'fail')
    else:
        flash(u'The email address you entered (' + email +') is a VALID email address. Thank you!', 'success')
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
            'email': email
        }
        mysql.query_db(query, data)
    return redirect('/')

@app.route('/delete/<email_id>', methods=['GET'])
def delete(email_id):
    query = "DELETE FROM emails WHERE id = :id"
    data = {'id': email_id}
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
