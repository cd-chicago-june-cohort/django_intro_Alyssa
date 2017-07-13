# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'survey/index.html')

def process(request):
    if request.method == 'POST':
        if "counter" not in request.session:
            request.session['counter']=1
        else:
            request.session['counter']+=1
        request.session['form'] = request.POST
        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    return render(request, 'survey/result.html')