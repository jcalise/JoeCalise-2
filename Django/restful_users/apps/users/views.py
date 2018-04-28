# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect,reverse,HttpResponse
from django.contrib import messages
from .models import *

def index(request):
    users = User.objects.all()
    return render(request, 'users/index.html', {'users': users})

def show(request, id):
    users = User.objects.get(id=id)
    return render(request, 'users/show.html', {'users': users})

def new(request):
    return render(request, 'users/new.html')

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect(reverse('new'))
    else:
        name = request.POST['fname'] + " " + request.POST['lname']
        user = User.objects.create(name=name, email=request.POST['email'])
        user.save()
        return redirect(reverse('index'))
    return redirect(reverse('index'))

def destroy(request, id):
    u = User.objects.get(id=id)
    u.delete()
    return redirect(reverse('index'))

def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, 'users/edit.html', {'user': user})

def update(request, id):
    u = User.objects.get(id=id)
    u.name = request.POST['name']
    u.email = request.POST['email']
    u.save()
    return redirect(reverse('index'))

