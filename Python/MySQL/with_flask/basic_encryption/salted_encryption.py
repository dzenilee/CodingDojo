# While md5 is an easy encryption method and safe for small-time projects, it is not secure enough
# for enterprise-level applications. To really secure your data, you need to make the encryption method
# more random. By random, we mean more unpredictable. As we said before, md5 encryption is the same
# no matter what computer runs the code. So to make our encryption more powerful, we will encrypt our
# data by using what is called a salt. A salt is a "unique" key used to generate a unique password. Example:
salt = '123'; # where the value 123 changes randomly
encrypted_password = md5(password . '' . salt);

# A salt is a string of random characters that will be passed to an encryption method (an md5())
# along with the string we are trying to encrypt (the submitted password) via concatenation.
# The encryption method that uses the salt is designed in such a way that it takes the salt to
# compute the encrypted string, using the salt as an 'ingredient' in the encryption 'recipe'.

# GENERATING A SALT
# To generate a salt, you just need to generate a random string of characters.
# The code below actually uses two different functions to render a random string:
import os, binascii # include this at the top of your file
salt = binascii.b2a_hex(os.urandom(15))

# The function called os.urandom() returns a string of bytes. The number of bytes is equal
# to the parameter provided. This string isn't a normal alphanumeric string, so we turn it into
# a string using the function b2a_hex(), which will turn the value returned from the openSSL
# function into a normal alphanumeric string. This new random string will be our salt.
# The idea is to store this salt during the registration process. Example:
username = request.form['username']
email = request.form['email']
password = request.form['password']
salt = binascii.b2a_hex(os.urandom(15))
encrypted_pw = md5.new(password + salt).hexdigest()
insert_query = "INSERT INTO users (username, email, password, salt, created_at, updated_at) VALUES (:username, :email, :encrypted_pw, :salt, NOW(), NOW())
query_data = {'username': username, 'email', email, 'encrypted_pw', encrypted_pw, 'salt': salt}
mysql.query_db(insert_query, query_data)

# Now, when we're trying to authenticate a uesr's login, we do some pretty nifty stuff:
email = request.form['email']
password = request.form['password']
user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
query_data = {'email': email}
user = mysql.query_db(user_query, query_data)
if user[0]:
    encrypted_password = md5.new(password + user[0]['salt']).hexdigest();
    if user[0]['password'] == encrypted_password:
    # this means we have a successful login!
    else:
    # invalid password!
else: # invalid email! 
