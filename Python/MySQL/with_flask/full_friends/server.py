from flask import Flask, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = 'full_friends_secret'
mysql = MySQLConnector(app, 'fullfriendsdb')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Display all of the friends on the index.html page
@app.route('/')
def index():
    # show all friends in DB
    all_query = "SELECT * FROM friends"
    all_stored = mysql.query_db(all_query)
    # all_friends is a variable in index.html 
    return render_template('index.html', all_friends = all_stored)

# Handle the add friend form submit and create the friend in the DB
@app.route('/friends', methods = ['POST'])
def create():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    # logic, validation
    if len(data['email']) < 1:
        flash('Email cannot be left blank!')
    elif not EMAIL_REGEX.match(data['email']):
        flash('Email is not valid!')
    else:
        # add a friend
        add_query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        mysql.query_db(add_query, data)
        # show success message
        flash('Your information was successfully submitted.')
    return redirect('/')

# DISPLAY the edit friend page for a particular friend
@app.route('/friends/<id>/edit')
def edit(id):
    query = "SELECT * FROM friends WHERE id = :id"
    data = {'id': id}
    record = mysql.query_db(query, data)
    print record
    # select the first element in the record object (i.e., the only element)
    return render_template('edit.html', friend = record[0])

# Handle the edit friend from submit and update the friend in the DB
@app.route('/friends/<id>', methods = ['POST'])
def update(id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
    # Define a dictionary with key that matches :variable_name in query.
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': id,
    }
    record = mysql.query_db(query, data)
    return redirect('/')

# Delete the friend from the DB
@app.route('/friends/<id>/delete', methods = ['POST'])
def destroy(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
