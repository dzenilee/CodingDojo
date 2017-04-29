from flask import Flask, render_template, request, redirect, session, flash
import random
import time

app = Flask(__name__)
app.secret_key = 'this_is_a_secret_ninja_gold'

@app.route('/')
def index():
    if 'gold_counter' not in session:
        session['gold_counter'] = 0
    if 'result' not in session:
        session['result'] = (0, "")
    if 'message' not in session:
        session['message'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    #logic check
    #at casino:
    if request.form['building'] == 'casino':
        session['randomCasino'] = random.randrange(-50,51)
        session['result'] = (session['randomCasino'], 'casino')
        session['gold_counter'] += session['randomCasino']
        #if loss
        if session['randomCasino'] < 0:
            session['message'].append("Entered a casino and lost {} golds. ({})".format(session['result'][0], time.strftime("%Y/%m/%d %I:%M:%S%p")))
        #if gain or broke even
        elif session['randomCasino'] >= 0:
            session['message'].append("Earned {} from the casino! ({})".format(session['result'][0], time.strftime("%Y/%m/%d %I:%M:%S%p")))
    #at other than casino:
    else:
        if request.form['building'] == 'farm':
            session['randomFarm'] = random.randrange(10,21)
            session['result'] = (session['randomFarm'], 'farm')
            session['gold_counter'] += session['randomFarm']
        elif request.form['building'] == 'cave':
            session['randomCave'] = random.randrange(5,11)
            session['result'] = (session['randomCave'], 'cave')
            session['gold_counter'] += session['randomCave']
        elif request.form['building'] == 'house':
            session['randomHouse'] = random.randrange(2,6)
            session['result'] = (session['randomHouse'], 'house')
            session['gold_counter'] += session['randomHouse']
        session['message'].append("Earned {} golds from {}! ({})".format(session['result'][0], session['result'][1], time.strftime("%Y/%m/%d %I:%M:%S%p")))

    #update counter
    if 'gold_counter' not in session:
        session['gold_counter'] = 0

    #print to console
    print session['message']
    print "Your Gold is", session['gold_counter']
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
