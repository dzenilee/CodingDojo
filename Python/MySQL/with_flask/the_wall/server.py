from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'TheWall_secreT!'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'walldb')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    # validate name
    if len(first_name) < 2:
        flash('You must enter a valid first name')
    elif len(last_name) < 2:
        flash('You must enter a valid last name')
    # validate email
    if len(email) < 1:
        flash('Email cannot be left blank')
    elif not EMAIL_REGEX.match(email):
        flash('You must enter a valid email address')
    # if all validations successful
    else:
        # create password hash with bcrypt
        pw_hash = bcrypt.generate_password_hash(password)
        # insert new user into DB with pw_hash
        add_user_query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        # create a dictionary of data from the POST data received
        user_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'pw_hash': pw_hash
        }
        record = mysql.query_db(add_user_query, user_data)
        print 'printing record:', record # print user's id
        session['id'] = record
        flash('You have successfully registered!')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = {
        'email': email,
    }
    record = mysql.query_db(query, data) # list containing a single dictionary of key-value pairs pertaining to user trying to log in [{u'pw_hash': u'$2b$12$dfkdjfk',
    # u'first_name': u'Jenny', u'last_name': u'Lee',
    # u'created_at': datetime.datetime(2017, 5, 10, 7, 54, 59),
    # u'updated_at': datetime.datetime(2017, 5, 10, 7, 54, 59),
    # u'email': u'dzenilee@gmail.com',
    # u'password': None, u'id': 1L}]
    print record
    if not record:
        flash('Your email and password do not match/exist! Try again.')
        return redirect('/')
    elif bcrypt.check_password_hash(record[0]['pw_hash'], password):
        session['id'] = record[0]['id']
        session['first_name'] = record[0]['first_name']
        session['last_name'] = record[0]['last_name']
        return redirect('/wall')

@app.route('/wall')
def wall():
    # message query and data
    msg_query = "SELECT messages.id, messages.message, DATE_FORMAT(messages.created_at, '%M %d, %Y %h:%i %p') as time_created, messages.updated_at, CONCAT(users.first_name, ' ', users.last_name) AS author FROM messages LEFT JOIN users on users.id = messages.user_id ORDER BY messages.created_at DESC"
    all_msg_records = mysql.query_db(msg_query)

    # comment query and data
    comment_query = ("SELECT comments.id, comments.message_id, comments.comment, DATE_FORMAT(comments.created_at, '%M %d %Y %h:%i %p') AS time_created, comments.updated_at, CONCAT(users.first_name, ' ', users.last_name) AS commenter FROM comments "
        "JOIN users ON comments.user_id = users.id "
        "ORDER BY comments.created_at ASC")
    all_comment_records = mysql.query_db(comment_query)
    return render_template('wall.html', all_msg_contents = all_msg_records, all_comment_contents = all_comment_records)

@app.route('/post_message', methods=['POST'])
def post_message():
    message = request.form['message']
    user_id = session['id']
    print 'this is the user id', user_id
    # print type(user_id) # int
    # validate message
    if len(message) < 1:
        flash('Write a message!')
    else:
        # add a message to DB
        # don't forget to specify user_id
        add_message = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
        data = {
            'message': message,
            'user_id': user_id
        }
        record = mysql.query_db(add_message, data) # a record of new message in a list
        print 'this is the message id:', record
    return redirect('/wall')

@app.route('/post_comment', methods=['POST'])
def post_comment():
    comment = request.form['comment']
    message_id = request.form['message_id']
    user_id = session['id']
    if len(comment) < 1:
        flash('Write a comment!')
    else:
        # add a comment to DB
        add_comment = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW())"
        data = {
            'comment': comment,
            'user_id': user_id,
            'message_id': message_id
        }
        record = mysql.query_db(add_comment, data)
        print 'this is the comment id:', record
    return redirect('/wall')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
