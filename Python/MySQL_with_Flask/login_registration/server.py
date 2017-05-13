from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'login_reg_secrEt!'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'reglogindb')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # get user data from form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    # run validations and if they're successful, create the password hash with bcrypt
    # validate name
    if len(first_name) < 2:
        flash('First name cannot be left blank!')
    elif len(last_name) < 2:
        flash('Last name cannot be left blank!')
    # validate email
    if len(email) < 1:
        flash('Email cannot be left blank!')
    elif not EMAIL_REGEX.match(email):
        flash('Email is not valid!')
    # if all validations successful
    else:
        # create password hash with bcrypt
        pw_hash = bcrypt.generate_password_hash(password)
        # now we insert the new user into the database with pw_hash:
        add_query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        # create a dictionary of data from the POST data received
        query_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'pw_hash': pw_hash
        }
        # record of new user in a list
        record = mysql.query_db(add_query, query_data)
        print 'this is my record: ', record # prints id number 
        flash('Congratulations! You have successfully created a new account.')
        # place new record (user) in session
        # session['id'] = record[0]['id']
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = {
        'email': email
    }
    # return user record in a list
    record = mysql.query_db(user_query, query_data)
    # If both the password and the existing password hash are a match, log in user.
    if bcrypt.check_password_hash(record[0]['pw_hash'], password):
        # login user
        print 'password hash:', record[0]['pw_hash']
        # 'user' is the variable that's in the success template
        return render_template('success.html', user=record[0]['first_name'])
    else:
        flash('Your email and password do not match! Try again.')
        return redirect('/')

app.run(debug=True)
