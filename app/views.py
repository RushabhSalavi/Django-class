from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1> Good Morning </h1>')

def about(request):
    return HttpResponse('About page')