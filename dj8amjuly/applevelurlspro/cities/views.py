from django.shortcuts import render

from django.http.response import HttpResponse


def hyd(request):
    x="hyderabad is famous city for all courses"
    return HttpResponse(x)
def bang(request):
    y="banglore is famous for all kind for jobs"
    return (request)





