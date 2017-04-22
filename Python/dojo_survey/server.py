from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "thisismysecretkey!!!"

@app.route('/')
def index():
    return render_template('index.html')

#this route handles form submission
@app.route('/result', methods=['POST'])
def create_user():
    if len(request.form['name']) < 1:
        flash("Please enter your name.")
        return redirect('/')
    if len(request.form['comment']) > 120:
        flash("Comments have to be fewer than 120 characters.")
        return redirect('/')
    else:
        print "post info"
        name = request.form['name']
        location = request.form['location']
        language = request.form['language']
        comment = request.form['comment']
        # return render_template('result.html')
        return render_template('result.html', name = name, location = location, language = language, comment = comment)

app.run(debug=True) #run our server
