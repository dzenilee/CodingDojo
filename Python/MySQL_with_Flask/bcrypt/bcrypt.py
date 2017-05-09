# Now that we understand the basics of salted encryption, we can use bcrypt
# which is a powerful module that helps us to encrypt our passwords in a secure way!

# Now to use bcrypt in our Flask Apps we can do this:
from flask import Flask, request, render_template
from mysqlconnection import MySQLConnector
# imports the Bcrypt module
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'my_database_here')

# this will load a page that has 2 forms, one for registration and one for login
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    # We are going to add functions to create new users and login users

# Now we can use the provided bcrypt functions to create encrypted passwords
# and authenticate when a user is signing in

# generate_password_hash
@app.route('/create_user', methods=['POST'])
def create_user():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    # run validations and if they are successful, we can create the password hash with bcrypt
    pw_hash = bcrypt.generate_password_hash(password)
    # now we insert the new user into the database:
    insert_query = "INSERT INTO users (email, username, pw_hash, created_at) VALUES (:email, :username, :pw_hash, NOW())"
    # create a dictionary of data from the POST data received
    query_data = {'email': email, 'username': username, 'pw_hash': pw_hash}
    mysql.query_db(insert_query, query_data)
    # redirect to success page

# check_password_hash
# The check_password_hash function will return true if the hashed value of
# password provided at login is equal to the password hash in the database.
# Otherwise, it will return false. The function works like this:
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = {'email': email}
    user = mysql.query_db(user_query, query_data) # user will be returned in a list
    if bcrypt.check_password_hash(user[0]['pw_hash'], password):
        # login user
    else:
        # set flash error message and redirect to login page 
