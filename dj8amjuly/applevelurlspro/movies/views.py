from django.shortcuts import render

from django.http.response import HttpResponse
def bahubali(request):
    x="bahubali is very hit movie in 2018"
    return HttpResponse(x)
def RAW(request):
    y="Raw is famous movie in 2019"
    return HttpResponse(y)
def MissionMangal(request):
    z="Mission mangal is famous movie in 2019"
    return HttpResponse(z)
