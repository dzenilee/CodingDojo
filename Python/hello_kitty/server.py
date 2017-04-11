from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "I<3Secrets" # needed for flash messages

@app.route('/')
def index():
    if "counter" not in session:
        session["counter"] = 0 # count how many times you add someone to our site. The first time you go through, counter is zero.
    print "I'm in my route for index!"
    return render_template("index.html") # showing it right away

@app.route('/users', methods = ["POST"])
def new_user():
    if len(request.form["first_name"]) == 0:
        flash("FILL ME IN! I NEED A NAME!")
        return redirect('/') # redirect to place that renders it (i.e., index.html)
    print request.form["first_name"]
    print request.form["id"]
    # session["first_name"].append('jonathan') # session is a way to store information and utilize it later. session is just a dictionary
    session["counter"] += 1 # increase counter each time we go through.
    # route should handle one thing, either showing info or collecting info to show somewhere else.
    # print session["first_name"]
    print
    return redirect('/success')
    # return redirect('/success') # once you got information, route to get to success.html. # doesn't work

@app.route('/success') # redirect to new route, for showing the information. Show success user's page, where they've been added.
def show_user():
    # print "in success route", session["first_name"]
    return render_template("success.html")
    # you can also show all the users in the database

app.run(debug=True, port=8000)
