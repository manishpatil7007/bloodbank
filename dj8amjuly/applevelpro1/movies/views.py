from django.shortcuts import render

from django.http.response import HttpResponse
def bahubali(request):
    x="prabhas hit movie."
    return HttpResponse(x)
def sahoo(request):
    y="prabhas and shrdha "
    return HttpResponse(y)
def vastav(request):
    z="sanjubaba movie"
