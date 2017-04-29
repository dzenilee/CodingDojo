from flask import Flask, render_template, request, redirect, session, flash
from random import randint

app = Flask(__name__)
app.secret_key = "secrets_secrets"

@app.route('/')
def index():
    #we want the random # to be created just one time.
    if "number" not in session:
        session['number'] = randint(1,100)
    print session['number'], 'This is the random number'
    return render_template('index2.html')

@app.route('/guess', methods=['POST'])
def numberGuess():
    #store user's guess
    guess = int(request.form['guess'])
    #logic check
    if guess < session['number']:
        print 'in low if'
        session['guess'] = 'low'
    elif guess > session['number']:
        print 'in high elif'
        session['guess'] = 'high'
    else:
        print 'in match'
        session['guess'] = 'match'
    return redirect('/')

@app.route('/reset', methods=['GET'])
def newGame():
    session.clear()
    # session.pop('someKey')
    return redirect('/')

app.run(debug=True, port=8888)
