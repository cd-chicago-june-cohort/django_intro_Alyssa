# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    request.session['products'] = [
        {'item':'Dojo Tshirt', 'price':19.99, 'id':1}, 
        {'item':'Dojo Sweater', 'price':29.99, 'id':2},
        {'item':'Dojo Cup', 'price':4.99, 'id':3},
        {'item':'Algorithm Book', 'price':49.99, 'id':4},
        ]
    request.session['price_to_id'] = {'1':19.99, '2':29.99, '3':4.99, '4':49.99}
    return render(request, 'amadon_app/index.html')

def buy(request, product_id):
    if request.method == 'POST':
        request.session['current_quantity']= request.POST['quantity']
        request.session['current_price'] = (request.session['price_to_id'][product_id] * float(request.session['current_quantity']))
        print request.session['current_price']
        return redirect('/checkout')
    else:
        return redirect('/')

def checkout(request):
    try:
        request.session['total_quantity'] += int(request.session['current_quantity'])
        request.session['total_cost'] += float(request.session['current_price'])
    except:
        request.session['total_quantity'] = int(request.session['current_quantity'])
        request.session['total_cost'] = float(request.session['current_price'])
    return render(request, 'amadon_app/checkout.html')
