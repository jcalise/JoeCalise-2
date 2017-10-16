# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if "counter" not in request.session:
        request.session["counter"] = 1
    else:
        request.session["counter"] += 1

    context = {
       "word": get_random_string(length=12)
       }
    return render(request,'rand_word/index.html', context)

def reset(request):
    request.session["counter"] = 0
    return redirect('/')
