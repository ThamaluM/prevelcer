from django.shortcuts import render
from django.http import HttpResponse
from fcm_django.models import FCMDevice

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello Welcome to our home page!</h1> - Thamalu, Helik, Buddhini, Adrian.") #"Hello Welcome"



def send_notification(request):
    device = FCMDevice.objects.all(request.GET["username"])
    device.send_message(request.GET["title"], request.GET["message"])
    return HttpResponse("Success")
    