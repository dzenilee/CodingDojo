from flask import Flask, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = 'TheWall_secreT!'
mysql = MySQLConnector(app, 'walldb')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app.run(debug=True)

@app.route('/')
def index():
    query = "SELECT messages.message,  "
    return render_template('index.html')
