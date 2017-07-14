# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

def index(request):
    try:
        all_words = request.session['words']
    except:
        request.session['words'] = []
    return render(request, 'words/index.html')

def add_word(request):
    if request.method == 'POST':
        new_word = {}
        new_word['word'] = request.POST['word']
        new_word['color'] = request.POST['color']
        new_word['size'] = request.POST['size']
        new_word['time'] = strftime('%H:%M %p, %b %D %Y', localtime())
        request.session['words'].insert(0, new_word)
        print '**1**'
        print request.session['words']
        request.session.modified = True
        return redirect('/')
    else:
        return redirect('/')

def clear(request):
    try:
        del request.session['words']
    except:
        request.session['words']=[]
    return redirect('/')