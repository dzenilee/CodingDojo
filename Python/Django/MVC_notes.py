"""
MVC

MTV stands for 'model template view', which describes the division of labor
in Django. See below for a description of what each element does.

In Django:

Model (Model)
View (Templates)
Controller (Views)

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
MODEL: builds database tables and handles all interaction with the database (Model)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
MODELS: are just like Django's models. Frameworks differ in what the model
layer does. In Django much of our logic that deals with the database is moved
to the model, while this may not be the case in other frameworks.

* Database
* Calls to the DB
* server connection file
* Validation (validate in the area where the info is housed)

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
VIEW: anything that deals with view of page (like templates) (Templates)
Templates are served in their complete form to the client.
Django's templating allows us to perform some logic and inject data into our
HTML documents.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
In other frameworks like Ruby on Rails, views are the equivalent of
Django templates. MVC frameworks attach the name views to the component *users
actually see*, versus the data that is sent to the client.

* Templates
    HTML
    Static files
        CSS
* Jinja Templating (Django Templating Engine)

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
CONTROLLER: handles logic (Views)
The views document is somewhat confusingly named, but can be thought of as
managing traffic. It is the view's job to get the right data for the right route
delivered in the right form. Views handle the data we deliver to the user to view.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
The MVC controller is roughly equivalent to Django's views. In both framework
types this component should be in charge of outsourcing work to the models and
sending the appropriately formatted data to the client. We mentioned that some
other frameworks don't outsource logic to the model. In those cases, many of
our logical operations are done in the controller.

-------
As you can see, although Django's terminology varies slightly from the usual
MVC pattern, the two are close enough that Django may be considered an MVC
framework. Although it is important to use the right term for each component,
we can think of Django as an MVC framework. 

* Importing modules
    Flask
    Secret Key
    render_template
    (Models)
* Declaration of server application
* Running application (app.run)
* Methods to do stuff
    render template
    redirect
    talk to DB
    set session

-------------------------------
Routing
    Index routing
    Advanced routing

"""
