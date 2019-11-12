from django.shortcuts import render
from .models import Empdata1
from .forms import Empform
from django.http.response import HttpResponse

def emp_view(request):
    if request.method=='POST':
        eform=Empform(request.POST)
        if eform.is_valid():
            ename1=request.POST.get('ename')
            sal1=request.POST.get('salary')
            mobile1=request.POST.get('mobile')
            email1=request.POST.get('email')
            location1=request.POST.get('location')
            data=Empdata1(
                ename=ename1,
                salary=sal1,
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





