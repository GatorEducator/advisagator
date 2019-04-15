""" This file allows us to write our own custom views for our HTML templates"""
# pylint: disable=W0611
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# pylint: disable=W0613
def index(request):
    """This is undocumented"""
    return HttpResponse("Hello, world. You're at the polls index.")
