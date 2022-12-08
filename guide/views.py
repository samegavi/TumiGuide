from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Place

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def place(request):
    #return HttpResponse("You're looking at a list of places")
    return render(request, "guide/places.html")

def topic(request):
    #return HttpResponse("You're looking at the list of topics")
    return render(request, "guide/topics.html")

def entry(request):
    #return HttpResponse("You're looking at table of entries")
    return render(request, "guide/entries.html")