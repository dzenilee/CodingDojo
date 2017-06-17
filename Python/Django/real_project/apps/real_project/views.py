# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
def index(request):
    print '#' * 50
    return render(request, 'real_project/index.html')

def testimonals(request):
    print request.method
    return render(request, 'real_project/testimonials.html')

def about(request):
    return render(request, 'real_project/about.html')

def projects(request):
    return render(request, 'real_project/projects.html')
