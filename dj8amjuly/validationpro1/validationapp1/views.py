from django.shortcuts import render
from .forms import RegistrationForm
from .models import RegistrationData
from django.http.response import HttpResponse

def RegForm_Page(request):
        if request.method == "POST":
            rform = RegistrationForm(request.POST or None)
            if rform.is_valid():
                print(rform.cleaned_data)
                firstname = rform.cleaned_data.get('firstname')
                lastname = rform.cleaned_data.get('lastname')
                username = rform.cleaned_data.get('username')
                email = rform.cleaned_data.get('email')
                password1 = rform.cleaned_data.get('password1')
                password2 = rform.cleaned_data.get('password2')
                mobile = rform.cleaned_data.get('mobile')
                data = RegistrationData(
                    firstname=firstname,
                    lastname=lastname,
                    username=username,
                    email=email,
                    password1=password1,
                    password2=password2,
                    mobile=mobile
                )
                data.save()
                rform = RegistrationForm()
                return render(request, 'feedback.html', {'rform': rform})
            else:
                return HttpResponse("Invalid Data")
        else:
            rform = RegistrationForm()
            return render(request, 'feedback.html', {'rform': rform})



