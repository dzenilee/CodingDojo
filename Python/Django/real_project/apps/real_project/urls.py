# ROUTES
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about, name='about'),
    url(r'^projects$', views.projects, name='projects'),
    url(r'^testimonials$', views.testimonals, name='testimonials')
]
