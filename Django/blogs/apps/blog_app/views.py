# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "Placeholder to later display all of the blogs"
    return HttpResponse(response)

def new(request):
    response = "Placeholder to display a form to create a new blog "
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, blog):
    response = "Placeholder to display blog " + blog
    return HttpResponse(response)

def edit(request, blog):
    response = "Placeholder to edit blog " + blog
    return HttpResponse(response)


def destroy(request, blog):
    return redirect('/')
