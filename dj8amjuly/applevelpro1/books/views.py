from django.shortcuts import render
from django.http.response import HttpResponse

def wingsonFire(request):
    x="wrote by abdul kalm sir"
    return HttpResponse(x)

def Jyotipunj(request):
    y="wrote by Narendra modi"
    return HttpResponse(y)

