from django.shortcuts import render
from .models import EmpData
from .forms import EmpForm

def emp_view(request):
    if request.method=="POST":
        eform=EmpForm(request.POST)
        eform.save()
        eform=EmpForm()
        return render(request,'emp.html',{'eform':eform})
    else:
        eform=EmpForm(request.POST)
        return render(request,'emp.html',{'eform':eform})



