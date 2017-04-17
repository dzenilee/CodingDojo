from flask import Flask, render_template, request, redirect, session, flash # import Flask object that is part of the flask module; render_template knows to look inside 'template' folder and render 'index.html'
app = Flask(__name__) # his is an object. Global variable __name__ tells Flask whether or not we are running the file directly or importing it as a module.
app.secret_key = "I<3Secrets"

@app.route('/') #how we want to access our server. The forward slash is the root of your application. The @ symbol designates a 'decorator' which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we run the following "hello_world" function.
def hello():
    #only if not in session do we want to set "users", else do nothing
    if "users" not in session:
        session['users'] = []
        session['counter'] = 1
    return render_template('index.html')

@app.route('/user', methods=['POST'])
def addUser():
    user = {
    "first_name": request.form['fname'],
    "last_name": request.form['lname'],
    "email": request.form['email'],
    'id': request.form['count'] #name is 'count', not 'counter'!
    }

    #do some validation
    if len(user['first_name']) < 2:
        flash('First name must be longer than 2 characters.')
    if len(user['last_name']) < 2:
        flash('Last name must be longer than 2 characters.')
    if "_flashes" in session: #the underscore: built-in key meaning once it's caught, it's gone
        return redirect('/') 

    #save this info to session
    session['user'] = user
    session['counter'] += 1
    print session['user']['first_name']
    #append user (which is an object) into list of all users -> so you get a list of objects
    session['users'].append(user)
    print session['users']
    print 'counter',
    return redirect('/')

#you want information about a specific user
@app.route('/user/<id>')
def showUser(id):
    #get the user with the id passed in
    for user in session['users']:
        if user['id'] == id:
            one_user = user
    #return a new page containing info about the specified user, send info about specified unser stored in variable one_user
    return render_template('user.html', user=one_user)

@app.route('/clear')
def clearSession():
    session.clear()
    return redirect('/')

app.run(debug=True, port=8888) # Run the app in debug mode. debug=True lets you see all the errors.
