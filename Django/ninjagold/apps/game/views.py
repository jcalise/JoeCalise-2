# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random

def index(request):
    # make sure that total_gold is in session, or create it
    try:
        request.session['total_gold']
    except KeyError:
        request.session['total_gold'] = 0

    return render(request, 'game/index.html')

def process_money(request, location):
    # make sure that activites is in session, or create it
    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []
    
    #assign current value of session.activities to temp variable activities
    activities = request.session['activities']

    if (location == "farm"):
        g = random.randrange(10,21)
        request.session['total_gold'] += g
        activities.append("You went to the " + location + " and earned " + str(g))
    elif (location == "cave"):
        g = random.randrange(5,11)
        request.session['total_gold'] += g
        activities.append("You went to the " + location + " and earned " + str(g))
    elif (location == "house"):
        g = random.randrange(2,6)
        request.session['total_gold'] += g
        activities.append("You went to the " + location + " and earned " + str(g))
    elif (location == "casino"):
        g = random.randrange(0,50)
        win = random.choice([True, False])
        if win:
            print("You won")
            request.session['total_gold'] += g
            activities.append("You went to the " + location + " and won " + str(g))
        else:
            print("You lost")
            request.session['total_gold'] -= g
            activities.append("You went to the " + location + " and lost " + str(g) + "! Ouch. :(")

    request.session['activities'] = activities
    return redirect('index')
