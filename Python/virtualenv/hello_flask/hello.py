from flask import Flask, render_template # import Flask object that is part of the flask module; render_template knows to look inside 'template' folder and render 'index.html'

app = Flask(__name__) # his is an object. Global variable __name__ tells Flask whether or not we are running the file directly or importing it as a module.

@app.route('/') #how we want to access our server. The forward slash is the root of your application. The @ symbol designates a 'decorator' which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we run the following "hello_world" function.

def hello_world():
    return render_template('index.html', name='Jenny') #render the template, pass data to template, and run it!
    # "{{name}}" in the HTML file will be replaced by the variable that we pass to the render_template function! With Flask, we can use templates to insert python code and python variables into our views!

app.run(debug=True, port=8888) # Run the app in debug mode. debug=True lets you see all the errors.

##############################################
# def numbers():
#     #pass # for now. Everything afterthis don't worry about
#     for number in range(3):
#         print "we're in number"
#     return redirect('/')

# return render_template('second.html')
