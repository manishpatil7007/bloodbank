from django.shortcuts import render
from .models import ServicesData1
from .models import EnquiryData
from.forms import EnquiryForm



def home_view(request):
    return render(request,'durgasoft1_home.html')


def enquiry_view(request):
    if request.method == 'POST':
        pass
    else:
        eform = EnquiryForm()
        return render(request, 'durgasoft1_contact.html', {'eform': eform})

    return render(request,'durgasoft1_contact.html')


def services_view(request):
    services=ServicesData1.objects.all()
    return render(request,'durgasoft1_services.html',{'servises':services})


def gallery_view(request):
    return render(request,'durgasoft1_gallery.html')


def feedback_view(request):
    return render(request,'durgasoft1_feedback.html')