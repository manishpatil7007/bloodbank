from django.shortcuts import render,redirect
from .models import RegistrationData
from .forms import RegistrationForm,LoginForm
from django.http.response import HttpResponse

def registration_view(request):
    if request.method=="POST":
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            first_name1=request.POST.get('first_name')
            last_name1=request.POST.get('last_name')
            username1=request.POST.get('username')
            password1=request.POST.get('password')
            email1=request.POST.get('email')
            mobile1=request.POST.get('mobile')
            data=RegistrationData(
                first_name=first_name1,
                last_name=last_name1,
                username=username1,
                password=password1,
                email=email1,
                mobile=mobile1
            )
            data.save()
            rform=RegistrationForm()
            return render(request,'reg.html',{'rform':rform})
        else:
            return HttpResponse("Invalid Data")
    else:
        rform=RegistrationForm()
        return render(request,'reg.html',{'rform':rform})

def login_view(request):
    if request.method=="POST":
        lform=LoginForm(request.POST)
        if lform.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')

            uname=RegistrationData.objects.filter(username=username)
            pwd=RegistrationData.objects.filter(password=password)

            if uname and pwd:
                return redirect('/home/')
            else:
                return HttpResponse("Wrong Details.")
        else:
                return HttpResponse("Invalid Data")
    else:
        lform=LoginForm()
        return render(request,'login.html',{'lform':lform})

def sucess_view(request):
    return render(request,'success.html')







