from django.shortcuts import render
from django.http import HttpResponse
from fcm_django.models import FCMDevice
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return HttpResponse('''
    <html><head><style>body {background-image: url('https://cdn.pixabay.com/photo/2016/11/18/12/06/white-male-1834117_960_720.jpg');}</style></head>
    <body>
    
    
    <center><h1>Hello Welcome to our home page!</h1>


     - Thamalu, Helik, Buddhini, Adrian.</center>
     </body></html>
     ''') #"Hello Welcome"



def send_notification(request):
    user = User.objects.get(username=request.GET["username"])
    device = FCMDevice.objects.filter(user=user).first()
    device.send_message(request.GET["title"], request.GET["message"])
    return HttpResponse("Success")
    