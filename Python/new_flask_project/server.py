from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'ljksdfj3k4jsdgg34'

import re #regex

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$') #raw string
# '+' = at least one
# '*' = 0 or more

@app.route('/')
def index():
    strings = ['hi there', 'wowie wow wow', 'hmm']

    for key in session:
        print "-------------\n", key

    try:
        #something that might break
        session['high_score']
    except:
        #if it broke, this is the code you want to execute
        print ('it broke')
        session['high_score'] = 0
    return render_template('index.html', my_list = strings)


@app.route('/dojo/new', methods=['POST'])
def new():
    print 'hello'
    print request.form
    
    if request.form['which_form'] == 'name_form':
        errors = []
        if len(request.form['text']) < 1: # same as if not len(request.form['text']):
            #send an error message
            flash('hey, you need to fill out your name on the form there')

        if len(request.form['email']) < 5:
            flash('email must be filled out')
        elif not EMAIL_REGEX.match(request.form['email']):
            flash('invalid email, try a more valid one')

        if '_flashes' not in session: # if we have flahsed any messages:
            session['name'] = request.form['text']
            session['high_score'] *= 2
    else:
        print "in age form"
        try:
            age = int(request.form['age'])
            print age, type(age)
        except ValueError: # in the event of a value error
            flash('put a number in the age form please!')
        session['age'] = request.form['age']

    return redirect('/')

app.run(debug=True)
