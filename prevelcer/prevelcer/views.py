from django.shortcuts import render
from django.http import HttpResponse
from fcm_django.models import FCMDevice
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello Welcome to our home page!</h1> - Thamalu, Helik, Buddhini, Adrian.") #"Hello Welcome"



def send_notification(request):
    user = User.objects.get(username=request.GET["username"])
    device = FCMDevice.objects.get(user=user)
    device.send_message(request.GET["title"], request.GET["message"])
    return HttpResponse("Success")
    