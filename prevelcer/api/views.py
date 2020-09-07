from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Welcome.") #"Hello Welcome"

def test_get(request):
    return JsonResponse({"message":"Hi this is really cool."})

