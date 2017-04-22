from flask import Flask, request, session, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def show_all_ninjas():
    img = '../static/img/all_ninjas.png'
    return render_template('ninja.html', img = img)

@app.route('/ninja/<color>')
def show_ninja(color):
    if color == 'blue':
        img = '../static/img/leonardo.jpg'
        ninja = 'Leonardo'
    elif color == 'red':
        img = '../static/img/raphael.jpg'
        ninja = 'Raphael'
    elif color == 'orange':
        img = '../static/img/michelangelo.jpg'
        ninja = 'Michelangelo'
    elif color == 'purple':
        img = '../static/img/donatello.jpg'
        ninja = 'Donatello'
    else:
        img = '../static/img/notapril.jpg'
        ninja = ''
    return render_template('ninja.html', img = img, ninja = ninja)


app.run(debug=True)
