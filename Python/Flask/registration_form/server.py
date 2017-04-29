from flask import Flask, render_template, request, redirect, session, flash
import re

#create a regular expression object that we can use to run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "regFormSecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit():
    #make sure all fields filled
    if len(request.form['first_name']) < 1:
        flash('You must enter a first name!')
    if len(request.form['last_name']) < 1:
        flash('You must enter a last name!')
    if len(request.form['password']) <= 8:
        flash('Passwords must be more than 8 characters!')
    #email validation
    if len(request.form['email']) < 1:
        flash('You must enter an email!')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('You must enter a VALID email!')
    #validate password has 1 uppercase and 1 numeric
    if not any(char.isupper() for char in request.form['password']):
        flash('You must have at least one upperclass letter!')
    if not any(char.isdigit() for char in request.form['password']):
        flash('You must have at least one number!')
    #validate password match
    if request.form['password'] != request.form['confirm_password']:
        flash('Your password does not match!')
    else:
        flash("Success!")
    return redirect('/')

app.run(debug=True)
