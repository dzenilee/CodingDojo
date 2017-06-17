# CONTROLLER: RECEIVE INCOMING REQUESTS AND SEND COLLECTED DATA BACK AS PART OF A TEMPLATE.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello_world/index.html')
