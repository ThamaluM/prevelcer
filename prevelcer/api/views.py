from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to our home page </h1>  <b> Let us prevent pressure ulcers. <b>Prevention is better than cure.</b>") #"Hello Welcome"

def test_get(request):
    return JsonResponse({"topic":"just_testing","message":"Hi this is really cool."})

