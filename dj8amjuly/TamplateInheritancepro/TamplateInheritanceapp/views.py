from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'myhome.html')

def contact(request):
    return render(request,'mycontact.html')

def feedback(request):
    return render(request,'myfeedback.html')

def gallary(request):
    return render(request,'mygallary.html')


