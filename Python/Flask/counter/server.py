from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "it'sasecret!"

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html')

@app.route('/more', methods=['POST'])
def more_counters():
    if request.form['counter'] == 'incrementBy2':
        session['counter'] += 1
    elif request.form['counter'] == 'reset':
        session['counter'] = 0
    return redirect('/')

app.run(debug=True)
