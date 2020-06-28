from django.shortcuts import render
from django.http import HttpResponse

# home controls traffic of the homepage


def home(request):
    return HttpResponse('<h1>Hello World</h1>')


def about(request):
    return HttpResponse('<h1>This is the about page</h1>')
