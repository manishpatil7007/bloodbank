from django.shortcuts import render

from django.http.response import HttpResponse
def valsad(request):
    x="famous for tourisam"
    return HttpResponse(x)
def Mumbai(request):
    y="famous for ganpati"
    return HttpResponse(y)
def Bang(request):
    z="famous for job"


