from django.shortcuts import render

from django.http.response import HttpResponse
def shreeyuva(request):
    x="famous from last 27 year  in tarabaugh"
    return HttpResponse(x)
def shreeMitra(request):
    y="famous from last 12 in maninagar"
    return HttpResponse(y)
def AhirYouth(request):
    z="famous as king of valsad"
    return HttpResponse(z)
