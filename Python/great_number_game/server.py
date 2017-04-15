from flask import Flask, render_template, request, redirect, session, flash
import random

app = Flask(__name__)
app.secret_key = 'thisismysecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    #store and print random number generated
    session['randomNum'] = random.randrange(0, 101)
    print "The random number generated is", session['randomNum']

    #store and print user's guess
    session['userGuess'] = int(request.form['number'])
    print "The user guessed", session['userGuess']

    #logic check
    if session['userGuess'] == session['randomNum']:
        print 'correct'
    elif session['userGuess'] > session['randomNum']:
        print 'too high!'
    elif session['userGuess'] < session['randomNum']:
        print 'too low!'
    return redirect('/')

app.run(debug=True)
