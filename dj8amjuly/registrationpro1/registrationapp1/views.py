from django.shortcuts import render
from .models import ManishData
from.forms import ManishForm
from django.http.response import HttpResponse

def Manish_view(request):
    if request.method=='POST':
        mform=ManishForm(request.POST)
        mform.save()
        mform=ManishForm()
        return render(request,'manish.html',{'mform':mform})
    else:
        mform=ManishForm(request.POST)
        return render(request,'manish.html',{'mform':mform})


