from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Mattress, ReportCycle, PressureEntry
from .serializers import PressureEntrySerializer
from rest_framework.response import Response
from datetime import datetime
import json


# Create your views here.

def insert(request):
    return HttpResponse("abracadbra nonsense.")

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

def read_mat(request):

    serial = request.GET["serial"].strip()
    n  = int(request.GET["n"])
    
    mat = Mattress.objects.get(serial=serial)
    n = ReportCycle.objects.get(mat=mat,id=n)

    entries = PressureEntry.objects.filter(mat=mat, n = n)
    result = {"data":[{"x":entry.x, "y":entry.y, "lx":entry.l_x, "ly":entry.l_y,"p":entry.p} for entry in entries] ,
    "status":'completed' if n.end_dt else "incompleted"}
    return JsonResponse(result)