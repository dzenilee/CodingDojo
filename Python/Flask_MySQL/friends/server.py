from flask import Flask, request, redirect, render_template, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector

app = Flask(__name__)

# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'friendsdb')

# an example of running a query
print mysql.query_db("SELECT * FROM friends")

@app.route('/')
def index():
    # Define your query
    query = "SELECT * FROM friends"
    # run query with query_db()
    friends = mysql.query_db(query)
    # Pass data into our template
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    # Run query, with dictionary values injected into the query.
    # Pass the query into the MySQL object's query_db function.
    mysql.query_db(query, data)
    return redirect('/')

# Inserting Data into Queries
@app.route('/friends/<friend_id>')
def show(friend_id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': friend_id}
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('friends.html', one_friend=friends[0])
    # Grabbing the friend_id from the URL and passing that
    # into the function as the same name as the URL parameter friend_id

@app.route('/update_friend/<friend_id>')
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation'],
        'id': friend_id
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
    query = 'DELETE FROM friends WHERE id = :id'
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
