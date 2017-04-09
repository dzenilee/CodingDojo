from flask import Flask, render_template # import Flask object that is part of the flask module
#render_template knows to look inside 'template' folder

app = Flask(__name__) # this is an object

@app.route('/') #how we want to access our server. The forward slash is the root of your application.

def hello():
    #return "Hello Flask!"
    # name = "Jonathan"
    age = 14
    return render_template('index.html', name = "Jonathan", age = age) #should print "I'm using Flask!" from index.html file in template folder on localhost.

@app.route('/numbers')
def numbers():
    #pass # for now. Everything afterthis don't worry about
    for number in range(3):
        print "we're in number"
    return redirect('/')

    # return render_template('second.html')

app.run(debug=True, port=8888) # only need it once at the end
                    #debug=True lets you see all the errors
