from django.shortcuts import render
from .models import EmpData
from .forms1 import Empform
from django.http.response import HttpResponse

def emp_view(request):
    if request.method=='POST':
        eform=Empform(request.POST)
        if eform.is_valid():
            ename1=request.post.get('ename')
            sal1=request.post.get('sal')
            mobile1=request.post.get('mobile')
            email1=request.post.get('email')
            location1=request.post.get('location')
            data=EmpData(
                ename=ename1,
                sal=sal1,
                mobile=mobile1,
                email=email1,
                location=location1,
            )
            data.save()
            eform=Empform()
            return render(request,'empdata.html',{'abcd':eform})
        else:
            return HttpResponse("User Invalid data")
    else:
        eform=Empform()
        return render(request,'empdata.html',{'abcd':eform})
