# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
    return render(request,'words/index.html')

def process(request):
    if request.method == "POST":
        if 'words' not in request.session:
            request.session['words'] = []

        try:
            size = request.POST['big']
        except:
            size = ""

        newWord = {
            'word': request.POST['word'],
            'color': request.POST['color'],
            'size': size,
            'time': datetime.now().strftime("%m/%d/%y @ %I:%M")
        }
        
        old = request.session['words']
        old.append(newWord)
        
        request.session['words'] = old
        
        return redirect("/results")
    else:
        return redirect("/")

def results(request):
    return render(request, 'words/results.html')

def clear(request):
    del request.session['words']
    return redirect('/')

