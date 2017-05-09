# do this in terminal
import m5 # imports the md5 module to generate a hash
password = 'password'
#encrypt the password we provided as 32 character string
encrypted_password = md5.new(password).hexdigest()
print encrypted_password # this will show you the encrypted value
# 5f4dcc3b5aa765d61d8327deb882cf99


# HOW TO USE md5
# When you add users to the database upon registration, you should save their passwords
# as an encrypted md5 string. Similarly, when they log in, you should encrypt the
# inputted password to make sure it matches with the one saved in the database.
# Here's the idea:

# The user being put into your database:
import md5
@app.route('/users/create', methods=['POST'])
def create_user():
    username = request.form['username']
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    insert_query = "INSERT INTO users (username, email, password, created_at, updated_at) VALUES (:username, :email, :password, NOW(), NOW())"
    query_data = {'username': username, 'email': email, 'password': password}
    mysql.query_db(insert_query, query_data)

# When your user is trying to log in:
password = md5.new(request.form['password']).hexdigest()
email = request.form['email']
user_query = "SELECT * FROM users WHERE users.email = :email AND users.password = :password"
query_data = { 'email': email, 'password': password}
user = mysql.query_db(user_query, query_data)
# do the necessary logic to login if the user exists,
# otherwise redirect to login page with error message 
