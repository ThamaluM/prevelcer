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

    mat = Mattress.objects.create(patient=request.user,serial=request.GET["serial"])
    return JsonResponse({"serial":mat.serial})


def start_cycle(request):
    serial = int(request.GET["serial"])
    n = int(request.GET["n"])
    time = datetime.now()
    mattress = Mattress.objects.get(serial=serial)
    ReportCycle.objects.create(mat=mattress,n=n,start_dt=time)
    return JsonResponse({"session":n, "status":"started"})

def end_cycle(request):

    serial = int(request.GET["serial"])
    n = int(request.GET["n"])
    mattress = Mattress.objects.get(serial=serial)
    report_cycle = ReportCycle.objects.get(mat=mattress,n=n)
    time = datetime.now()
    report_cycle.end_dt = time 
    report_cycle.save()

    return JsonResponse({"session":n, "status":"ended"})

def enter_data(request):

    serial = int(request.GET["serial"])
    n = int(request.GET["n"])
    x = int(request.GET["x"])
    y = int(request.GET["y"])
    l_x = int(request.GET["lx"])
    l_y = int(request.GET["ly"])
    p = float(request.GET["p"])

    mat = Mattress.objects.get(serial=serial)
    #n = ReportCycle.objects.get(mat=mat,n=n)

    PressureEntry.objects.create(mat=mat,n=n,x=x,y=y,l_x=l_x,l_y=l_y,p=p)

    return JsonResponse({"status": "Success"})

def read_mat(request):

    id = int(request.GET["id"])
    n  = int(request.GET["n"])
    
    mat = Mattress.objects.get(id=id)

    entries = PressureEntry.objects.filter(mat=mat, n = n)
    result = {"data":[{"x":entry.x, "y":entry.y, "lx":entry.l_x, "ly":entry.l_y,"p":entry.p} for entry in entries]}
    return JsonResponse(result)