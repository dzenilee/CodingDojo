pip install Django
    # installs Django package

pip list:
    appdirs (1.4.2)
    click (6.7)
    cycler (0.10.0)
    Django (1.10.6)
    Flask (0.12.1)
    itsdangerous (0.24)
    Jinja2 (2.9.5)
    MarkupSafe (1.0)
    matplotlib (2.0.0)
    monty (0.9.6)
    nltk (3.2.2)
    numpy (1.12.0)
    packaging (16.8)
    pip (9.0.1)
    pyparsing (2.1.10)
    python-dateutil (2.6.0)
    pytz (2016.10)
    setuptools (34.3.0)
    six (1.10.0)
    Werkzeug (0.12.1)

pip install Django:
Requirement already satisfied: Django in /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages

pip freeze:
appdirs==1.4.2
click==6.7
cycler==0.10.0
Django==1.10.6
Flask==0.12.1
itsdangerous==0.24
Jinja2==2.9.5
MarkupSafe==1.0
matplotlib==2.0.0
monty==0.9.6
nltk==3.2.2
numpy==1.12.0
packaging==16.8
pyparsing==2.1.10
python-dateutil==2.6.0
pytz==2016.10
six==1.10.0
Werkzeug==0.12.1

What's the difference between freeze and list?
# == instead of ()

First cd into your Desktop directory (cd ~/Desktop), then run this command: pip freeze > requirements.txt. What do you see when you ls? What's inside this file?
# Creates requirements.txt with the contents of freeze.

pip uninstall Django:
# uninstalls Django

pip show Django
# nothing happens

pip search Flask
# shows all the components of Flask with description
