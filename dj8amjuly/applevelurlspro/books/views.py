from django.shortcuts import render

from django.http.response import HttpResponse

def python(request):
    x="Python is a powerfull language."
    return HttpResponse(x)
def django(request):
    y="Django is a framework of python language."
    return HttpResponse(y)
def UI(request):
    z="ui is used in python for front end design."
    return HttpResponse
