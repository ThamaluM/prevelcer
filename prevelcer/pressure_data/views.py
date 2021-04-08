from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Mattress, ReportCycle, PressureEntry
from .serializers import PressureEntrySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from datetime import datetime
import json


# Create your views here.

def insert(request):
    return HttpResponse("Welcome to pressure data.")

@login_required
def register(request):

    mat = Mattress.objects.create(patient=request.user,serial=request.GET["serial"].strip())
    return JsonResponse({"serial":mat.serial})


def start_cycle(request):
    n=0  # Could not figure it out an additional need. To be removed
    serial = request.GET["serial"].strip()
    #n = int(request.GET["n"])
    time = datetime.now()
    mattress = Mattress.objects.get(serial=serial)
    rc = ReportCycle.objects.create(mat=mattress,n=n,start_dt=time)
    return JsonResponse({"session":rc.id, "status":"started"})

def end_cycle(request):

    serial = request.GET["serial"].strip()
    #n = int(request.GET["n"])
    mattress = Mattress.objects.get(serial=serial)
    report_cycle = ReportCycle.objects.filter(mat=mattress,end_dt=None)[0]
    time = datetime.now()
    report_cycle.end_dt = time 
    report_cycle.save()

    return JsonResponse({"session":report_cycle.id, "status":"ended"})

def enter_data(request):

    serial = request.GET["serial"].strip()
    n = int(request.GET["n"])
    x = int(request.GET["x"])
    y = int(request.GET["y"])
    l_x = int(request.GET["lx"])
    l_y = int(request.GET["ly"])
    p = float(request.GET["p"])

    mat = Mattress.objects.get(serial=serial)
    n = ReportCycle.objects.get(mat=mat,id=n, end_dt=None)

    PressureEntry.objects.create(mat=mat,n=n,x=x,y=y,l_x=l_x,l_y=l_y,p=p)

    return JsonResponse({"status": "Success"})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def read_mat(request):

    patient = User.objects.get(username=request.GET["patient"].strip())
    n  = int(request.GET["n"])
    
    mat = Mattress.objects.filter(patient=patient).last()
    n = ReportCycle.objects.get(mat=mat,id=n)

    entries = PressureEntry.objects.filter(mat=mat, n = n)
    result = {"data":[{"x":entry.x, "y":entry.y, "lx":entry.l_x, "ly":entry.l_y,"p":entry.p} for entry in entries] ,
    "status":'completed' if n.end_dt else "incompleted"}
    return JsonResponse(result)

@login_required
def read_current(request):

    patient = User.objects.get(username=request.GET["patient"].strip())

    


    mattress = Mattress.objects.filter(patient=patient).last()
    try:
        report_cycle = ReportCycle.objects.filter(mat=mattress,end_dt=None)[0]
    except:
        return HttpResponse('''<head><meta http-equiv="refresh" content="2"></head>''')
    entries = PressureEntry.objects.filter(mat=mattress, n = report_cycle)

    image = [
        [0.]*entries[0].l_x
       ]*entries[0].l_y

    for entry in entries:
      image[int(entry.y)-1][int(entry.x)-1] = int(entry.p)

    return render(request, "pressure_data/realtime.html", {"image":image})


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def read_mat_viz(request):

    patient = User.objects.get(username=request.GET["patient"].strip())
    



    mattress = Mattress.objects.filter(patient=patient).last()
    n = None
    try:
        n=request.GET["n"]
    except:
        pass
    if n is not None:
        report_cycle = ReportCycle.objects.get(mat=mattress,id=int(n))
    else:
        report_cycle = ReportCycle.objects.filter(mat=mattress).order_by('-n').first()
    
    entries = PressureEntry.objects.filter(mat=mattress, n = report_cycle)

    

    image = [
        [0.]*entries[0].l_x
       ]*entries[0].l_y

    for entry in entries:
      image[int(entry.y)-1][int(entry.x)-1] = int(entry.p)

    return Response({"image":image})