from django.shortcuts import render
from .models import EnquiryData
from .forms import EnquiryForm
from django.http.response import HttpResponse



def enquiry_view(request):
    if request.method=='POST':
        eform=EnquiryForm(request.POST)
        if eform.is_valid():
            name=request.POST.get('name')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            gender=request.POST.get('gender')
            courses=eform.cleaned_data.get('courses')
            shifts=eform.cleaned_data.get('shifts')
            start_date=eform.cleaned_data.get('start_date')
            data=EnquiryData(
                name=name,
                mobile=mobile,
                email=email,
                gender=gender,
                courses=courses,
                shifts=shifts,
                start_date=start_date

            )
            data.save()
            eform=EnquiryForm()
            return render(request, 'enquiry1.html', {'eform': eform})
        else:
            return HttpResponse("Invalid user.")
    else:
        eform=EnquiryForm()
        return render(request,'enquiry1.html',{'eform':eform})


def gallery_view(request):
    return render(request,'enquiry1.html')









