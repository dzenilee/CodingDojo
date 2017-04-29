from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret" # you need to set a secret key for security purposes

#routing rules and rest of server.py below.

#our index route will handle rendering our form
@app.route('/')
def index():
    return render_template('index.html')

#this route will handle our form submission
#notice how we defined which HTTP methods are allowed by this route

#1. Submitting the form takes you to the POST/users route which is handled by the create_user function where we store the POST data in session
#2. The create_user function then redirects you to the GET /show route which is handled by the show_user function where we render the user.html template passing along the necessary information to the view
@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    # name = request.form['name']
    # email = request.form['email']
    # Now change create_user function to use session:
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    #redirects back to the '/' route, i.e., to index.html
    # return redirect('/')
    # change where we redirect to so that we can go to the page that displays the name and email!
    return redirect('/show')


@app.route('/show')
def show_user():
	# return render_template('user.html', name="Jay", email='kpatel@codingdojo.com')
    # Let's modify our show_user function to use session instead of hard coding the data (that's the line above)
    return render_template('user.html', name = session['name'], email = session['email'])


app.run(debug=True) #run our server
