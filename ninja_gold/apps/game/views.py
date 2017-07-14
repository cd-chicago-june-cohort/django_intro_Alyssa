# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

def index(request):
    if 'gold_counter' not in request.session:
        request.session['gold_counter'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'game/index.html')

def process_money(request, location):
    if request.method == 'POST':
        time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        # Use random numbers to deterimine how much gold won or lost based on location
        if location == 'farm':
            gold = random.randint(10,20)
        elif location == 'cave':
            gold = random.randint(5,10)
        elif location == 'house':
            gold = random.randint(2,5)
        elif location == 'casino':
            gold = random.randint(-50,50)
        # Update the session gold_counter to reflect the change
        updated_gold = request.session['gold_counter']
        updated_gold = updated_gold + gold
        request.session['gold_counter'] = updated_gold
        # Write the activity html
        if gold > 0:
            activity_string = 'Earned {} golds from the {}! ({})'.format(gold, location, time)
            activity_class = 'green'
        elif gold < 0:
            gold = gold * -1
            activity_string = 'Entered a casino and lost {} golds . . . Ouch. ({})'.format(gold, time)
            activity_class='red'
        else:
            activity_string = 'You managed to break even at the casino.  No gold earned or lost!'
            activity_class='blue'
        # Update the session activities list to have the new activity first
        activity = {
            'class': activity_class,
            'string': activity_string
        }
        request.session['activities'].insert(0, activity)
        request.session.modified = True
        print "*" * 50
        print request.session['activities']
        print '*' * 50
        return redirect('/')
    else:
        return redirect('/')
