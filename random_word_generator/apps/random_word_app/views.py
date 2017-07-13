# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect  
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' not in request.session:
        request.session['counter']=0
    request.session['counter'] += 1
    request.session['random_word'] = get_random_string(length=14)
    return render(request, 'random_word_app/index.html')

def reset(request):
    request.session['counter'] = 0
    return redirect('/')