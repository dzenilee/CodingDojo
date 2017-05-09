from flask import Flask, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = 'SeCrEtKeY_eMaIl'
mysql = MySQLConnector(app, 'emaildb')

# an example of running a query:
print mysql.query_db("SELECT * FROM emails")

#create a regular expression object that we can use to run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    data = {
        'email': request.form['email']
    }
    if len(data['email']) < 1:
        flash('Email cannot be left blank!')
        return render_template('index.html')
    elif not EMAIL_REGEX.match(data['email']):
        flash('Email is not valid!')
        return render_template('index.html')
    else:
        # add an email
        add_email_query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        # run the query
        run_add_email_query = mysql.query_db(add_email_query, data)
        # show all emails
        show_all_query = "SELECT * FROM emails"
        # run show all emails query
        run_show_all_query = mysql.query_db(show_all_query)
        return render_template('success.html', all_emails = run_show_all_query)

app.run(debug=True)
