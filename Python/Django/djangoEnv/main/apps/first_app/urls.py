from django.conf.urls import url
from . import views # go get views. views are controller
# models -- views -- templates(control)

# the url method is similar to @app.route method in flask 
urlpatterns = [ url(r'^$', views.index) ]
