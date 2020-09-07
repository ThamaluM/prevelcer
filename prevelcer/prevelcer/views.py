from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello Welcome to our home page!</h1> - Thamalu, Helik, Buddhini, Adrian.") #"Hello Welcome"


